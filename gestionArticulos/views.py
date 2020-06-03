from django.shortcuts import render
from gestionArticulos.models import Media
from gestionUsuarios.models import UsuarioInfo, UsuarioUbicacion
from gestionArticulos.enums import CategoriaType

# Create your views here.
# Las vistas se encargarán de gestionar las peticiones y las respuestas de las páginas web de la aplicación.


def articles_results(request):
    """
    Devolverá al usuario 10 resultados por página de los artículos encontrados a traves de su búsqueda con tags o sin tags usando categorías.
    """

    if request.method == 'GET':
        consulta = request.GET.get('consulta')
        categoria = request.GET.get('categoria')
        pag = request.GET.get('p')
        articulos_ppag = 2  # Artículos por página
        articulos = None

        if consulta and categoria:
            if not pag:  # Mantenemos que el número de página exista
                pag = 1

            # Mantenemos que el número de página se encuentre por encima del límite inferior
            pag = int(pag)
            if pag < 1:
                pag = 1

            # Listamos los tags si se han utilizado. (separados por comas)
            if ',' in consulta:
                taglist = consulta.split(',')
                print(taglist)

            if categoria != "Todas":  # Filtramos por categoría.
                if ',' in consulta:  # Si se encuentran comas en la consulta, la búsqueda será por tags.
                    articulos = Media.objects.filter(categoria__exact=CategoriaType(categoria).name, tags__name__in=taglist)
                else:
                    articulos = Media.objects.filter(categoria__exact=CategoriaType(categoria).name, nombre__icontains=consulta)
            else:
                if ',' in consulta:
                    articulos = Media.objects.filter(tags__name__in=taglist)
                else:
                    articulos = Media.objects.filter(nombre__icontains=consulta)

            # Gestionamos las páginas y los resultados a mostrar en esta
            n_articulos = articulos.count()
            if n_articulos % articulos_ppag < 1.0:
                n_pags = int(n_articulos/articulos_ppag)
                if n_pags == 0:  # Si hay menos de 10 artículos, habrá una sola página.
                    n_pags = 1
            else:  # Si el resultado de artículos por página es impar y mayor que uno, añadimos una página más.
                n_pags = int(n_articulos/articulos_ppag)+1

            if pag > n_pags:  # Mantenemos el número de página debajo del límite superior.
                pag = n_pags

            articulos = articulos[(pag-1)*articulos_ppag:articulos_ppag] # Recoge los artículos por página a partir del índice especificado entre los artículos.

    print(articulos)
    return render(request, 'gestionArticulos/articles.html', {'consulta': consulta,
                                                              'categoria': categoria,
                                                              'p': pag,
                                                              'n_pags': n_pags,
                                                              'n_articulos': n_articulos,
                                                              'articulos': articulos})


def article(request):
    """
    Devolverá al usuario el artículo consultado con información del propietario y su ubicación.
    """

    if request.method == 'GET':
        id = request.GET.get('id')
        articulo = None
        usuarioinfo = None
        usuarioub = None

        if id:
            articulo = Media.objects.filter(media_id=id)
            if articulo:
                usuarioinfo = UsuarioInfo.objects.filter(
                    usuario=articulo[0].propietario)
                usuarioub = UsuarioUbicacion.objects.filter(
                    usuario=articulo[0].propietario)

    return render(request, 'gestionArticulos/article.html', {'articulo': articulo, 'usuarioinfo': usuarioinfo, 'usuarioub': usuarioub})
