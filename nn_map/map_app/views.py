import base64
import folium
from django.views.generic import TemplateView
from folium import IFrame


class MyMapFolium(TemplateView):
    template_name = 'map_app/my_nn.html'

    def get_context_data(self, **kwargs):
        nn_map = folium.Map(location=[56.326798, 44.006509],
                            zoom_start=12)
        # Кнопка отображения и скрытия маркеров
        button_script = """\
            <script>
                function toggleMarkers() {
                    var markers = document.getElementsByClassName('leaflet-marker-icon');
                    for (var i = 0; i < markers.length; i++) {
                        if (markers[i].style.display === 'block') {
                            markers[i].style.display = 'none';
                        } else {
                            markers[i].style.display = 'block';
                        }
                    }
                }
            </script>
            <button onclick="toggleMarkers()">Скрыть/показать маркеры</button>
        """

        nn_map.get_root().header.add_child(folium.Element(button_script))
        # Добавление маркеров и описаний с фото
        encoded_for_sluda = base64.b64encode(open('static/normal.jpg', 'rb').read()).decode()
        html_for_sluda = '<h1>Водопад в парке "Швейцария"</h1>' \
                         '<center><img src="data:image/jpeg;base64,{}"></center>' \
                         'В теплое время года по каменной кладке подпорной стены бывшей железной дороги' \
                         ' текут грунтовые воды.' \
                         'Зимой на этом месте появляются водопады из сосулек и ледяные наросты.'.format
        popup_for_sluda = folium.Popup(IFrame(html_for_sluda(encoded_for_sluda), width=300, height=400), max_width=2650)
        encoded_for_hutor = base64.b64encode(open('static/hutor.jpg', 'rb').read()).decode()
        html_for_hutor = '<h1>Щелковский хутор</h1>' \
                         '<center><img src="data:image/jpeg;base64,{}"></center>' \
                         'Щёлоковский хутор» — это архитектурно-этнографический музей-заповедник,' \
                         ' расположенный в Нижнем Новгороде.'.format
        popup_for_hutor = folium.Popup(IFrame(html_for_hutor(encoded_for_hutor), width=300, height=400), max_width=2650)
        folium.Marker([56.268677, 44.009243], popup=popup_for_hutor).add_to(nn_map)
        folium.Marker([56.280208, 43.970620], popup=popup_for_sluda).add_to(nn_map)
        return {'map': nn_map._repr_html_()}

