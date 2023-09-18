#!/usr/bin/python3.8
from datetime import datetime, date

class PartyMember:
  def __init__(self, name, age, country, city, occupation):
    self.name = name
    self.age = age
    self.country = country
    self.city = city
    self.occupation = occupation

def add_interest(self, interest):
  self.interest = interest

def add_to_party(self):
  self.date_ent = datetime.now().date()

def __str__(self):
  return f'Comrade {self.name} from {self.city}({self.country}) joined us on the {self.date_ent}'
