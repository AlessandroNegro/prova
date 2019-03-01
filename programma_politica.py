name=input("inserisci il tuo nome")
print("...")
print("ciao",name,"benvenuto i questo programma, questa avventura ti permetterà di simulare un vita da politico, NB:questo programma non rappresenta la realtà.")
print("l'obbiettivo consiste nel restare al potere il piu a lungo possibile, dovrai rispettare le tue ideologie, non fare la figura del bugiardo, però attento a non attirarti l'ira delle persone che non la pensano esattamente come te!")
print("ed ora, iniziamo!")
print("")
print("")
part=input("inserisci il nome del tuo nuovo partito.")
print("")
print("")
print("complimenti",name,"hai fondato il",part)
print("...")
print("e ora inserisci l'orientamento del tuo partito")
orient=input("1)SINISTRA,2)CENTRO SINISTRA,3)CENTRO,4)CENTRO DESTRA,5)DESTRA")
if orient=="1":
	ide="sinistra"
elif orient=="2":
	ide="centro sinistra"
elif orient=="3":
	ide="centro"
elif orient=="4":
	ide="centro destra"
else:
	ide="destra"
print("")
print("il tuo partito ha un'ideologia di",ide)
print("")
print(name,"sei stato nominato/a segretario del",part,"ovvero il nuovo partito di",ide)
print("sono state appena effettuate le elezioni, e il tuo partito ha vinto con il 51%","dei voti")
perc=int(51)
print("...")
if orient=="1":
	print("MESE 1,")
	print("...")
	print("...")
	print("nonostante sia passato poco tempo dalle tue elezioni, si inizia subito con le interviste")
	print("giornalista:compliemnti per l'elezione, uno dei temi piu affrontati in politica è quello della gestione delle tasse, cosa intende fare da nuovo presidente?",)
	rtax=input("RISPONDO: 1)intendo abbassare moltissimo le tasse, perchè i cittadinti devono regalare soldi allo stato? 2)penso che in questo momento i cittadini paghino il giusto non indendo apportare modifiche,  3)la tasse sono troppo basse, intendo alzarle notevolmente ")
	if rtax=="1":
		print("nonostante, qualche parere contrario riesci a guadgnare l'appoggio di un altro buon 3%","della popolazione")
		perc=perc+3
	elif rtax=="2":
		print("il tuo partito ha un ideologia di sinistra, i tuoi sostenitori non si aspettavano questa risposta, i tuoi sostenitori sono calati dell'8%")
		perc=perc-8
	elif rtax=="3":
		print("le tue risposte contraddicono la tua ideologia, questo on pice ai tuoi sostenitori, e l'opposizione sfrutta questa occasione per accusarti, i tuoi sostenitori calano del 28%")
		perc=perc-24
	print("...")
	print("cosa intendi FARE realmente?")
	rtv=input("1)le abbasso notevolmente.  2)le lascio invariate.  3)le alzo")
	print("...")
	print("")
	print("")
	print("MESE 2, percentuale della popolazione a tuo favore:",perc,"%")
	print("...")
	if rtax==rtv:
		print("sei onesto, le tue azioni rispecchaino quelllo che fai, la popolazione a tuo favore aumenta del 2%")
		perc=perc+2
	else:
		print("le tue azioni non rispecchaino quello che dici,  la popolazione a tuo favore cala del 6%")
		perc=perc-7
	print("...")
	pippo=input("premi invio per avanzare di mese")
	if perc>20:
		pass
	else:
		print("la percentuale della popolazione a tuo favore è bassissima, ovvero il",perc,"%","scoppia una rivolta in tutto lo stato, ti catturano e poi ti esiliano.")
		print("GAME OVER,SEI SOPRAVVISUTO 2 MESI, CHE SCHIFOO")
		x=input("")
		while x!="grissinbon":
			print("chiudere il gioco!")
			x=input("")
	print("...")
	print("")
	print("")
	print("MESE 3, percentuale della popolazione a tuo favore:",perc,"%")
	print("...")
	print("la classe proletaria del tuo stato è in sciopero, sono presenti grossi disagi in tutte le città devi fare qualcosa!")
	print("...")
	rscio=input("COSA FAI?   1)non tolleriamo scioperi in questo paese li vieto tutti, per chi verrà sorpreso scioperare saranno presi seri provvedmenti.  2)Ognuno ha il diritto di scioperare, non prenderò provvedimenti")
	if rscio=="1":
		print("le tue azioni non rispecchaino l'ideologia del tuo partito, la percentuale della popolazione a tuo favore cala del 9%")
		perc=perc-9
	else:
		print("a causa dei forti disagi causati dagli scioperi, la popolazione a tuo favore cala del 5%")
		perc=perc-9
	print("...")
	pippo=input("premi invio per avanzare di mese")
	if perc>20:
		pass
	else:
		print("la percentuale della popolazione a tuo favore è bassissima, ovvero il",perc,"%","scoppia una rivolta in tutto lo stato, ti catturano e poi ti esiliano.")
		print("GAME OVER,SEI SOPRAVVISUTO 3 MESI, LA VITA POLITICA NON FA PER TE")
		x=input("")
		while x!="grissinbon":
			print("chiudere il gioco!")
			x=input("")
	print("...")
	print("")
	print("")
	print("MESE 4, percentuale della popolazione a tuo favore:",perc,"%")
	print("...")
	if rtv=="1":
		print("le tasse sono troppo basse, e i soldi dello stato non sono sufficenti per mantenere sufficentemente tutti i servizi del paese, i cittadini sono molto arrabbiati e sei obbligato ad alzare le tasse, tutto ciò causa una diminuzione delle persone a tuo favore del 10%")
		perc=perc-10
	elif rtv=="3":
		print("le tasse nel tuo paese sono alte, ciò rende i servizi del paese veramente ottimali, la popolazione a tuo favore aumenta del 6%")
		perc=perc+6
	else:
		print("in questo mese non succede nulla di particolare")
	print("...")
	pippo=input("premi invio per avanzare di mese")
	if perc>20:
		pass
	else:
		print("la percentuale della popolazione a tuo favore è bassissima, ovvero il",perc,"%","scoppia una rivolta in tutto lo stato, ti catturano e poi ti esiliano.")
		print("GAME OVER, SEI SOPRAVVISUTO 4 MESI, INSOMMA...")
		x=input("")
		while x!="grissinbon":
			print("chiudere il gioco!")
			x=input("")
	print("...")
	print("")
	print("")
	print("MESE 5, percentuale della popolazione a tuo favore:",perc,"%")
elif orient=="2":
	print("QUESTA OPZIONE NON E' ANCORA DISPONIBILE, MA LO SARA' A BERVE")
	pass
elif orient=="3":
	print("QUESTA OPZIONE NON E' ANCORA DISPONIBILE, MA LO SARA' A BERVE")
	pass
elif orient=="4":
	print("QUESTA OPZIONE NON E' ANCORA DISPONIBILE, MA LO SARA' A BERVE")
	pass
else:
	print("QUESTA OPZIONE NON E' ANCORA DISPONIBILE, MA LO SARA' A BERVE")
	pass
