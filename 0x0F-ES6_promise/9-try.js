#!/usr/bin/node
function guardrail(mathFunction) {
  const que = [];
  const Msg = 'Guardrail was processed';
  try {
    const obj = mathFunction();
    que.push(obj, Msg);
  } catch (err) {
    que.push(`Error: ${err.message}`, Msg);
  }
  return que;
}
export { guardrail as default };
