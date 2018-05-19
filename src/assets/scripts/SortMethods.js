export default {
  sortByName(centro1, centro2) {
    return centro1.nome.localeCompare(centro2.nome);
  },
  sortByTime(centro1, centro2) {
    return centro1.osm.tiempo < centro2.osm.tiempo ? -1 : 1;
  },
  sortByDistance(centro1, centro2) {
    return centro1.osm.distancia < centro2.osm.distancia ? -1 : 1;
  }
}
