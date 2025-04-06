# -*- coding: utf-8 -*-
{
    "name": "Películas",
    "summary": "Módulo para la gestión de películas e integración con API externa",
    "description": """
        Este módulo permite gestionar películas en Odoo:
        - Consulta películas desde un servicio REST externo (cron job cada minuto)
        - Registro de películas en un modelo propio (movie.movie)
        - Exposición de un endpoint REST (/api/top_movies) para obtener el top 10 de películas según ranking
    """,
    "author": "OsmaniCR",
    "website": "https://github.com/OsmaniCR/odoo-movies",
    "category": "Tools",
    "version": "1.0",
    "license": "LGPL-3",
    "depends": ["base", "web"],
    "external_dependencies": {
        "python": ["requests"],
    },
    "icon": "/movie_module/static/src/img/image.png",
    "data": [],
    "demo": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}
