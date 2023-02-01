from foreignkey_model import Pet, Owner, Toy, db

db.create_all()

sib = Pet('Siberian Husky')
hm = Pet('Himalayan flying squirrel')
rs = Pet('Rat snake')
db.session.add_all([sib, hm, rs])
db.session.commit()

catnip = Toy('Catnip', sib.id)
tug = Toy('Tug Toy', hm.id)
ss = Toy('Snake Skin', rs.id)
db.session.add_all([catnip, tug, ss])
db.session.commit()

mukesh = Owner('Mukesh', sib.id)
vinod = Owner('Vinod', hm.id)
raj = Owner('Raj', rs.id)
db.session.add_all([mukesh, vinod, raj])
db.session.commit()

if __name__=='__main__':
    print(sib)
    print(hm)
    print(rs)