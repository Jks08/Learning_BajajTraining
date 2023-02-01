from pet_model import Pet, db

db.create_all()

sib = Pet('Husky', 'Huky', 'Mukesh',2)
hm = Pet('Himalayan flying squirrel', 'Hafahafa', 'Vinod',2)
rs = Pet('Rat snake', 'Rattler', 'Raj',2)
db.session.add_all([sib, hm, rs])
db.session.commit()

if __name__=='__main__':
    print(f"{sib.pet_name} has ID {sib.pet_id} . It belongs to the {sib.pet_breed} familia and is {sib.pet_age} years old. It is owned by {sib.pet_owner}.")
