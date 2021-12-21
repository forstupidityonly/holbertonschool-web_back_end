export default function cleanSet(set, startString) {
  let rez = '';
  if (!startString || !startString.length) return rez;
  set.forEach((i) => {
    if (i && i.startsWith(startString)) rez += `${i.slice(startString.length)}-`;
  });
  return rez.slice(0, rez.length - 1);
}
