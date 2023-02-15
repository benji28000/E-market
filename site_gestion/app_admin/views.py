
from django.http import FileResponse
from django.utils import timezone
import pytz
from django.urls import reverse
from django.shortcuts import render,redirect
from gestion.models import Article,Panier,Achat
from gestion.froms import ArticleForm
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.shortcuts import get_object_or_404
from reportlab.pdfgen import canvas
from io import BytesIO


def dashboard(request):
    return render(request,'dashboard.html')

def user_articles(request):
    if not request.user.is_authenticated:
        return redirect('home')
    else:
        liste_articles=Article.objects.filter(user=request.user)
        liste_notarticles=Article.objects.exclude(user=request.user)
        return render(request,'my_articles.html',{'liste_articles':liste_articles,'liste_not_articles':liste_notarticles})


    
class AddArticle(CreateView):
    model=Article
    form_class = ArticleForm
    template_name ="add-article.html"
    success_url='../my_articles'

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)


class UpdateArticle(UpdateView):
    model=Article
    form_class=ArticleForm
    template_name='app_admin/formulaire_article.html'
    success_url='/myadmin/my_articles/'

class DeleteArticle(DeleteView):
    model=Article
    success_url='/myadmin/my_articles/'
    template_name='supprimer_article.html'


def add_panier(request, id):
    achat = get_object_or_404(Article, id=id)
    panier = Panier.objects.filter(user=request.user).first()
    if panier is None:
        panier = Panier.objects.create(user=request.user)
    order, est_crée = Achat.objects.get_or_create(user=request.user, article=achat,panier=panier)
    if est_crée:
        panier.achats.add(order)
        panier.save()
    else:
        if order.user == request.user and panier.achats.filter(id=order.id).exists():
            order.quantité_achat += 1
            order.save()
        else:
            panier.achats.remove(order)
    return redirect('detail',id)

def panier(request):
    user = request.user
    panier = Panier.objects.filter(user=user).first()
    achats = panier.achats.all() if panier else []
    context = {
        'achats': achats
    }
    return render(request, 'panier.html', context)


def ajouter_achat(request, achat_id):
    achat = get_object_or_404(Achat, id=achat_id)
    article=achat.article
    if achat.quantité_achat<article.quantité:

        achat.quantité_achat += 1
        achat.save()
    else:
       return redirect('panier')
    return redirect('panier')

def retirer_achat(request, achat_id):
    achat = get_object_or_404(Achat, id=achat_id)
    if achat.quantité_achat > 1:
        achat.quantité_achat -= 1
        achat.save()
    else:
        achat.delete()
    return redirect('panier')


def generer_pdf(request):
    user = request.user
    panier = get_object_or_404(Panier, user=user)
    achats = panier.achats.all()

    buffer = BytesIO()

    facture = canvas.Canvas(buffer)

    facture.drawString(100, 750, "Récapitulatif de vos achats")

    # Ligne horizontale en dessous du titre
    
    facture.line(80, 740, 510, 740)

    # Coordonnées du premier article
    y = 690
    facture.drawString(100, 720, f"article")
    facture.drawString(200, 720, f"quantité")
    facture.drawString(300, 720, f"prix unitaire")
    facture.drawString(400, 720, f"prix total par article")
    facture.line(80, 710, 510, 710)
    for achat in achats:
        article = achat.article
        facture.drawString(100, y, f"{article.title}")
        facture.drawString(200, y, f"{achat.quantité_achat}")
        facture.drawString(300, y, f"{article.prix} €")
        facture.drawString(400, y, f"{article.prix * achat.quantité_achat} €")
        y -= 20

    facture.line(80, y, 510, y)

    # Total
    total = sum([achat.article.prix * achat.quantité_achat for achat in achats])
    facture.drawString(400, y - 20, f"Total: {total} €")

    facture.line(80, y - 30, 510, y - 30)

    
    time_france=pytz.timezone('Europe/Paris')
    date_achat = timezone.now().astimezone(time_france).strftime('%d/%m/%Y %H:%M')
    facture.drawString(80, y - 50, f"Date d'achat: {date_achat}")

    facture.showPage()
    facture.save()

    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='recap_achat.pdf')