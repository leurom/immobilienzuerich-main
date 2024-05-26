## Immobilien Zürich - Koeffizientenberechnung

Dieses Flask-Projekt ermöglicht es, den "Koeffizienten" für einen bestimmten Standort im Kanton Zürich zu berechnen. Der Koeffizient basiert auf der Anzahl von Immobilien in der Nähe des ausgewählten Standorts.

**Funktionalitäten:**

* Zeigt eine interaktive Karte des Kantons Zürich mithilfe von Leaflet.
* Ermöglicht das Verschieben eines Markers, um einen Standort auszuwählen.
* Sendet die Koordinaten des ausgewählten Standorts an den Server.
* Berechnet den Koeffizienten basierend auf der Anzahl von Immobilien in einem Umkreis von 1 Kilometer um den ausgewählten Standort.
* Zeigt den berechneten Koeffizienten auf der Webseite an.

**Voraussetzungen:**

* Python 3.x
* Flask
* GeoPandas
* Shapely
* Leaflet (JavaScript-Bibliothek)
* jQuery (JavaScript-Bibliothek)

**Anwendungsbeispiel:**

1. Anwendung starten mit `python app.py`.
2. Öffnen der Anwendung in Ihrem Webbrowser (normalerweise `http://127.0.0.1:5000/`).
3. Marker auf der Karte verschieben, um den gewünschten Standort auszuwählen.
4. Auf Button "Koeffizient berechnen" klicken.
5. Der Koeffizient wird unterhalb der Karte angezeigt.

**Hinweise:**

* Diese Anwendung verwendet Beispieldaten und dient lediglich der Veranschaulichung.
* In einer realen Anwendung müssten die Immobiliendaten aus einer geeigneten Quelle geladen werden.
* Der Koeffizient kann je nach Anwendungsfall angepasst werden.


**Weitere Informationen:**

* Flask: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
* GeoPandas: [https://geopandas.org/](https://geopandas.org/)
* Shapely: [https://shapely.readthedocs.io/](https://shapely.readthedocs.io/)
* Leaflet: [https://leafletjs.com/](https://leafletjs.com/)
* jQuery: [https://jquery.com/](https://jquery.com/)
