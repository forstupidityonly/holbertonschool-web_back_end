import getListStudentIds from './1-get_list_student_ids';

export default function getStudentIdsSum(studentList) {
  const studentIds = getListStudentIds(studentList);
  const simmer = (acc, currVal) => acc + currVal;
  return studentIds.reduce(simmer);
}
