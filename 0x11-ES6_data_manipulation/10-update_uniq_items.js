export default function updateItems(map) {
  if (!(map instanceof Map)) throw Error('Cannor process');
  map.forEach((value, key) => {
    if (value === 1) { map.set(key, 100); }
  });
}
