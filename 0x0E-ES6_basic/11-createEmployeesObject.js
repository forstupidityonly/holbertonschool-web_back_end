#!/usr/bin/node
export default function createEmployeesObject(departmentName, employees) {
  const employe = {
    [departmentName]: employees,
  };
  return employe;
}
