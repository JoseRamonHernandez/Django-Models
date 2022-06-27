from django.shortcuts import render, HttpResponse, redirect
from Series.models import Series

# Create your views here.


def crear_series(request, serie_name, serie_clasificacion, serie_num_capitulos, serie_num_temporadas):
    serie = Series(
        serie_name = serie_name,
        serie_clasificacion = serie_clasificacion,
        serie_num_capitulos = serie_num_capitulos,
        serie_num_temporadas = serie_num_temporadas
    )
    
    serie.save()

    return HttpResponse(f"Serie Creada: <strong>{serie.serie_name}<br>Clasificación: {serie.serie_clasificacion}<br>Numero de capitulos: {serie.serie_num_capitulos}<br>Numero de temporadas{serie.serie_num_temporadas}<br>Fecha de registro: {serie.serie_created_at}</strong>")

def serie(request):
    try:
        Consultaserie = Series.objects.get(serie_name="Stranger Things")
        response = f"Serie: {Consultaserie.id}.{Consultaserie.serie_name}"
    except:
        response = "<h1>Serie Not Found</h1>"
    
    return HttpResponse(response)

def actualizar_Serie(request, id):

    buscarSerie = Series.objects.get(pk=id)

    buscarSerie.serie_name = "Peaky Blinders"
    buscarSerie.serie_clasificacion = "+18"

    buscarSerie.save()

    return HttpResponse(f"Serie Actualizada: <strong>{buscarSerie.serie_name}<br>Clasificación: {buscarSerie.serie_clasificacion}<br>Numero de capitulos: {buscarSerie.serie_num_capitulos}<br>Numero de temporadas{buscarSerie.serie_num_temporadas}<br>Fecha de registro: {buscarSerie.serie_created_at}</strong>")

def Serie_Found(request, id):

    buscarSerie = Series.objects.get(pk=id)
    return HttpResponse(f"Serie Buscada: <strong>{buscarSerie.serie_name}<br>Clasificación: {buscarSerie.serie_clasificacion}<br>Numero de capitulos: {buscarSerie.serie_num_capitulos}<br>Numero de temporadas: {buscarSerie.serie_num_temporadas}<br>Fecha de registro: {buscarSerie.serie_created_at}</strong>")

def all_series(request):

    allSeries = Series.objects.all()


    return render(request, 'series.html', {
        'serie': allSeries
    })

def delete_serie(request, id):
    serie= Series.objects.get(pk=id)
    serie.delete()

    return redirect('series')