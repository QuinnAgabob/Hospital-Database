"""DESCRIPTION OF THE MODULE GOES HERE

Author: Quinn Agabob
Class: CSI-260-01
Assignment: Week 4 Lab
Due Date: February 9, 2020 11:59 PM

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""
import pickle
import zipcodes
import phonenumbers

class Patients:
  patient_id = 1
  _all_patients = {}
  # __init__
  def __init__(self, fname, lname, address, ename, ephone, zip='10570', pnumber='9144879099'):
    # public variables
    self.fname = fname
    self.lname = lname
    self.address = address
    self.pnumber = phonenumbers.parse(pnumber, 'US')
    self.ename = ename
    self.ephone = ephone
    if zipcodes.is_real(zip):
      self.zip = zip
    self.fullName = fname + ' ' + lname

    #private variables
    self._id = Patients.patient_id
    Patients.patient_id = Patients.patient_id + 1
    self._procedures = []
    Patients._all_patients.update({self._id: self})
  # print statement
  def __str__(self):
    x = ('Name: ' + self.fname + ' ' + self.lname + '\nAddress: ' + self.address
           + '\nPhone Number: ' + str(self.pnumber) + '\nEmergency Contact Name' +
           self.ename + '\nEmergency Contact Number: ' + str(self.ephone) +
           '\nID: ' + str(self._id) + '\n')
    for y in range(len(self._procedures)):
      x = x + (self._procedures[y].__str__())
    return(x)

  def add_procedure(self, procedure):
    self._procedures.append(procedure)

  @classmethod
  def get_patient(cls, id):
    if id in Patients._all_patients:
      return Patients._all_patients[id]
    else:
      return None

  def delete_patient(self, ID):
    del Patients._all_patients[ID]
  def load_patients(self):
    with open('AllPatients.pickle', 'rb') as handle:
        Procedure._all_patients = pickle.load(handle)

  def save_patients(self):
    with open('AllPatients.pickle', 'wb') as handle:
      pickle.dump(Patients._all_patients, handle, protocol=pickle.HIGHEST_PROTOCOL)


class Procedure:
  procedure_id = 1
  _all_procedures = []
  def __init__(self, date, docName, cost):
    # public variables
    self.date = date
    self.docName = docName
    self.cost = cost

    #private variables
    self._id = Procedure.procedure_id
    Procedure.procedure_id = Procedure.procedure_id +1
    Procedure._all_procedures.append(self)
  def __str__(self):
    return ('Date: ' + str(self.date) + '\nDoctor Name: ' + self.docName + '\nCost: ' + str(self.cost) + '\nID: ' + str(self._id) + '\n')
patient1 = Patients('John', 'Smith', '97 Ashland', 'Grace', '911')
procedure1 = Procedure('2/2/22', ' James Smith', 3133)
patient1.add_procedure(procedure1)
procedure2 = Procedure('3/3/23', ' Connor Smith', 4000)
patient1.add_procedure(procedure2)
