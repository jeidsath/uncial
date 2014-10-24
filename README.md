uncial
======

Command line tool to convert Greek text to uncial

## Usage ##

```
cat input.txt > ./uncial.py > output.txt
```

## Example Input ##

```
<p> <span class="milestone chapter">1</span>Δαρείου καὶ Παρυσάτιδος γίγνονται παῖδες δύο, πρεσβύτερος μὲν Ἀρταξέρξης, νεώτερος δὲ Κῦρος· ἐπεὶ δὲ ἠσθένει Δαρεῖος καὶ ὑπώπτευε τελευτὴν τοῦ βίου, ἐβούλετο τὼ παῖδε ἀμφοτέρω παρεῖναι. <span class="milestone section">2</span>ὁ μὲν οὖν πρεσβύτερος παρὼν ἐτύγχανε· Κῦρον δὲ μεταπέμπεται ἀπὸ τῆς ἀρχῆς ἧς αὐτὸν σατράπην ἐποίησε, καὶ στρατηγὸν δὲ αὐτὸν ἀπέδειξε πάντων ὅσοι ἐς Καστωλοῦ πεδίον ἁθροίζονται. ἀναβαίνει οὖν ὁ Κῦρος λαβὼν Τισσαφέρνην ὡς φίλον, καὶ τῶν Ἑλλήνων ἔχων ὁπλίτας ἀνέβη τριακοσίους, ἄρχοντα δὲ αὐτῶν Ξενίαν Παρράσιον. <span class="milestone section">3</span>ἐπεὶ δὲ ἐτελεύτησε Δαρεῖος καὶ κατέστη εἰς τὴν βασιλείαν Ἀρταξέρξης, Τισσαφέρνης διαβάλλει τὸν Κῦρον πρὸς τὸν ἀδελφὸν ὡς ἐπιβουλεύοι αὐτῷ. ὁ δὲ πείθεται καὶ συλλαμβάνει Κῦρον ὡς ἀποκτενῶν· ἡ δὲ μήτηρ ἐξαιτησαμένη αὐτὸν ἀποπέμπει πάλιν ἐπὶ τὴν ἀρχήν. <span class="milestone section">4</span>ὁ δ’ ὡς ἀπῆλθε κινδυνεύσας καὶ ἀτιμασθείς, βουλεύεται ὅπως μήποτε ἔτι ἔσται ἐπὶ τῷ ἀδελφῷ, ἀλλά, ἢν δύνηται, βασιλεύσει ἀντ’ ἐκείνου. Παρύσατις μὲν δὴ ἡ μήτηρ ὑπῆρχε τῷ Κύρῳ, φιλοῦσα αὐτὸν μᾶλλον ἢ τὸν βασιλεύοντα Ἀρταξέρξην. <span class="milestone section">5</span>ὅστις δ’ ἀφικνεῖτο τῶν παρὰ βασιλέως πρὸς αὐτὸν πάντας οὕτω διατιθεὶς ἀπεπέμπετο ὥστε αὐτῷ μᾶλλον φίλους εἶναι ἢ βασιλεῖ. καὶ τῶν παρ’ ἑαυτῷ δὲ βαρβάρων ἐπεμελεῖτο ὡς πολεμεῖν τε ἱκανοὶ εἴησαν καὶ εὐνοϊκῶς ἔχοιεν αὐτῷ. <span class="milestone section">6</span>τὴν δὲ Ἑλληνικὴν δύναμιν ἥθροιζεν ὡς μάλιστα ἐδύνατο ἐπικρυπτόμενος, ὅπως ὅτι ἀπαρασκευότατον λάβοι βασιλέα. ὧδε οὖν ἐποιεῖτο τὴν συλλογήν. ὁπόσας εἶχε φυλακὰς ἐν ταῖς πόλεσι παρήγγειλε τοῖς φρουράρχοις ἑκάστοις λαμβάνειν ἄνδρας Πελοποννησίους ὅτι πλείστους καὶ βελτίστους, ὡς ἐπιβουλεύοντος Τισσαφέρνους ταῖς πόλεσι. καὶ γὰρ ἦσαν αἱ Ἰωνικαὶ πόλεις Τισσαφέρνους τὸ ἀρχαῖον ἐκ βασιλέως δεδομέναι, τότε δὲ ἀφειστήκεσαν πρὸς Κῦρον πᾶσαι πλὴν Μιλήτου· <span class="milestone section">7</span>ἐν Μιλήτῳ δὲ Τισσαφέρνης προαισθόμενος τὰ αὐτὰ ταῦτα βουλευομένους ἀποστῆναι πρὸς Κῦρον, τοὺς μὲν αὐτῶν ἀπέκτεινε τοὺς δ’ ἐξέβαλεν. ὁ δὲ Κῦρος ὑπολαβὼν τοὺς φεύγοντας συλλέξας στράτευμα ἐπολιόρκει Μίλητον καὶ κατὰ γῆν καὶ κατὰ θάλατταν καὶ ἐπειρᾶτο κατάγειν τοὺς ἐκπεπτωκότας. καὶ αὕτη αὖ ἄλλη πρόφασις ἦν αὐτῷ τοῦ ἁθροίζειν στράτευμα. <span class="milestone section">8</span>πρὸς δὲ βασιλέα πέμπων ἠξίου ἀδελφὸς ὢν αὐτοῦ δοθῆναι οἷ ταύτας τὰς πόλεις μᾶλλον ἢ Τισσαφέρνην ἄρχειν αὐτῶν, καὶ ἡ μήτηρ συνέπραττεν αὐτῷ ταῦτα· ὥστε βασιλεὺς τὴν μὲν πρὸς ἑαυτὸν ἐπιβουλὴν οὐκ ᾐσθάνετο, Τισσαφέρνει δ’ ἐνόμιζε πολεμοῦντα αὐτὸν ἀμφὶ τὰ στρατεύματα δαπανᾶν· ὥστε οὐδὲν ἤχθετο αὐτῶν πολεμούντων. καὶ γὰρ ὁ Κῦρος ἀπέπεμπε τοὺς γιγνομένους δασμοὺς βασιλεῖ ἐκ τῶν πόλεων ὧν Τισσαφέρνους ἐτύγχανεν ἔχων. <span class="milestone section">9</span>ἄλλο δὲ στράτευμα αὐτῷ συνελέγετο ἐν Χερρονήσῳ τῇ κατ’ ἀντιπέρας Ἀβύδου τόνδε τὸν τρόπον. Κλέαρχος Λακεδαιμόνιος φυγὰς ἦν· τούτῳ συγγενόμενος ὁ Κῦρος ἠγάσθη τε αὐτὸν καὶ δίδωσιν αὐτῷ μυρίους δαρεικούς. ὁ δὲ λαβὼν τὸ χρυσίον στράτευμα συνέλεξεν ἀπὸ τούτων τῶν χρημάτων καὶ ἐπολέμει ἐκ Χερρονήσου ὁρμώμενος τοῖς Θρᾳξὶ τοῖς ὑπὲρ Ἑλλήσποντον οἰκοῦσι καὶ ὠφέλει τοὺς Ἕλληνας· ὥστε καὶ χρήματα συνεβάλλοντο αὐτῷ εἰς τὴν τροφὴν τῶν στρατιωτῶν αἱ Ἑλλησποντιακαὶ πόλεις ἑκοῦσαι. τοῦτο δ’ αὖ οὕτω τρεφόμενον ἐλάνθανεν αὐτῷ τὸ στράτευμα. <span class="milestone section">10</span>Ἀρίστιππος δὲ ὁ Θετταλὸς ξένος ὢν ἐτύγχανεν αὐτῷ, καὶ πιεζόμενος ὑπὸ τῶν οἴκοι ἀντιστασιωτῶν ἔρχεται πρὸς τὸν Κῦρον καὶ αἰτεῖ αὐτὸν εἰς δισχιλίους ξένους καὶ τριῶν μηνῶν μισθόν, ὡς οὕτως περιγενόμενος ἂν τῶν ἀντιστασιωτῶν. ὁ δὲ Κῦρος δίδωσιν αὐτῷ εἰς τετρακισχιλίους καὶ ἓξ μηνῶν μισθόν, καὶ δεῖται αὐτοῦ μὴ πρόσθεν καταλῦσαι πρὸς τοὺς ἀντιστασιώτας πρὶν ἂν αὐτῷ συμβουλεύσηται. οὕτω δὲ αὖ τὸ ἐν Θετταλίᾳ ἐλάνθανεν αὐτῷ τρεφόμενον στράτευμα. <span class="milestone section">11</span>Πρόξενον δὲ τὸν Βοιώτιον ξένον ὄντα ἐκέλευσε λαβόντα ἄνδρας ὅτι πλείστους παραγενέσθαι, ὡς ἐς Πισίδας βουλόμενος στρατεύεσθαι, ὡς πράγματα παρεχόντων τῶν Πισιδῶν τῇ ἑαυτοῦ χώρᾳ. Σοφαίνετον δὲ τὸν Στυμφάλιον καὶ Σωκράτην τὸν Ἀχαιόν, ξένους ὄντας καὶ τούτους, ἐκέλευσεν ἄνδρας λαβόντας ἐλθεῖν ὅτι πλείστους, ὡς πολεμήσων Τισσαφέρνει σὺν τοῖς φυγάσι τοῖς Μιλησίων. καὶ ἐποίουν οὕτως οὗτοι.</p>
```

## Example Output ##

```
ΔΑΡΕΙΟΥΚΑΙΠΑΡΥΣΑΤΙΔΟΣΓΙΓΝΟΝΤΑΙΠΑΙΔΕΣΔΥΟΠΡΕΣΒΥΤΕΡΟΣΜΕΝΑΡΤΑΞΕΡΞΗΣΝΕΩΤΕΡΟΣΔΕΚΥΡΟΣΕΠΕΙΔΕΗΣΘΕΝΕΙΔΑΡΕΙΟΣΚΑΙΥΠΩΠΤΕΥΕΤΕΛΕΥΤΗΝΤΟΥΒΙΟΥΕΒΟΥΛΕΤΟΤΩΠΑΙΔΕΑΜΦΟΤΕΡΩΠΑΡΕΙΝΑΙΟΜΕΝΟΥΝΠΡΕΣΒΥΤΕΡΟΣΠΑΡΩΝΕΤΥΓΧΑΝΕΚΥΡΟΝΔΕΜΕΤΑΠΕΜΠΕΤΑΙΑΠΟΤΗΣΑΡΧΗΣΗΣΑΥΤΟΝΣΑΤΡΑΠΗΝΕΠΟΙΗΣΕΚΑΙΣΤΡΑΤΗΓΟΝΔΕΑΥΤΟΝΑΠΕΔΕΙΞΕΠΑΝΤΩΝΟΣΟΙΕΣΚΑΣΤΩΛΟΥΠΕΔΙΟΝΑΘΡΟΙΖΟΝΤΑΙΑΝΑΒΑΙΝΕΙΟΥΝΟΚΥΡΟΣΛΑΒΩΝΤΙΣΣΑΦΕΡΝΗΝΩΣΦΙΛΟΝΚΑΙΤΩΝΕΛΛΗΝΩΝΕΧΩΝΟΠΛΙΤΑΣΑΝΕΒΗΤΡΙΑΚΟΣΙΟΥΣΑΡΧΟΝΤΑΔΕΑΥΤΩΝΞΕΝΙΑΝΠΑΡΡΑΣΙΟΝΕΠΕΙΔΕΕΤΕΛΕΥΤΗΣΕΔΑΡΕΙΟΣΚΑΙΚΑΤΕΣΤΗΕΙΣΤΗΝΒΑΣΙΛΕΙΑΝΑΡΤΑΞΕΡΞΗΣΤΙΣΣΑΦΕΡΝΗΣΔΙΑΒΑΛΛΕΙΤΟΝΚΥΡΟΝΠΡΟΣΤΟΝΑΔΕΛΦΟΝΩΣΕΠΙΒΟΥΛΕΥΟΙΑΥΤΩΙΟΔΕΠΕΙΘΕΤΑΙΚΑΙΣΥΛΛΑΜΒΑΝΕΙΚΥΡΟΝΩΣΑΠΟΚΤΕΝΩΝΗΔΕΜΗΤΗΡΕΞΑΙΤΗΣΑΜΕΝΗΑΥΤΟΝΑΠΟΠΕΜΠΕΙΠΑΛΙΝΕΠΙΤΗΝΑΡΧΗΝΟΔΩΣΑΠΗΛΘΕΚΙΝΔΥΝΕΥΣΑΣΚΑΙΑΤΙΜΑΣΘΕΙΣΒΟΥΛΕΥΕΤΑΙΟΠΩΣΜΗΠΟΤΕΕΤΙΕΣΤΑΙΕΠΙΤΩΙΑΔΕΛΦΩΙΑΛΛΑΗΝΔΥΝΗΤΑΙΒΑΣΙΛΕΥΣΕΙΑΝΤΕΚΕΙΝΟΥΠΑΡΥΣΑΤΙΣΜΕΝΔΗΗΜΗΤΗΡΥΠΗΡΧΕΤΩΙΚΥΡΩΙΦΙΛΟΥΣΑΑΥΤΟΝΜΑΛΛΟΝΗΤΟΝΒΑΣΙΛΕΥΟΝΤΑΑΡΤΑΞΕΡΞΗΝΟΣΤΙΣΔΑΦΙΚΝΕΙΤΟΤΩΝΠΑΡΑΒΑΣΙΛΕΩΣΠΡΟΣΑΥΤΟΝΠΑΝΤΑΣΟΥΤΩΔΙΑΤΙΘΕΙΣΑΠΕΠΕΜΠΕΤΟΩΣΤΕΑΥΤΩΙΜΑΛΛΟΝΦΙΛΟΥΣΕΙΝΑΙΗΒΑΣΙΛΕΙΚΑΙΤΩΝΠΑΡΕΑΥΤΩΙΔΕΒΑΡΒΑΡΩΝΕΠΕΜΕΛΕΙΤΟΩΣΠΟΛΕΜΕΙΝΤΕΙΚΑΝΟΙΕΙΗΣΑΝΚΑΙΕΥΝΟΙΚΩΣΕΧΟΙΕΝΑΥΤΩΙΤΗΝΔΕΕΛΛΗΝΙΚΗΝΔΥΝΑΜΙΝΗΘΡΟΙΖΕΝΩΣΜΑΛΙΣΤΑΕΔΥΝΑΤΟΕΠΙΚΡΥΠΤΟΜΕΝΟΣΟΠΩΣΟΤΙΑΠΑΡΑΣΚΕΥΟΤΑΤΟΝΛΑΒΟΙΒΑΣΙΛΕΑΩΔΕΟΥΝΕΠΟΙΕΙΤΟΤΗΝΣΥΛΛΟΓΗΝΟΠΟΣΑΣΕΙΧΕΦΥΛΑΚΑΣΕΝΤΑΙΣΠΟΛΕΣΙΠΑΡΗΓΓΕΙΛΕΤΟΙΣΦΡΟΥΡΑΡΧΟΙΣΕΚΑΣΤΟΙΣΛΑΜΒΑΝΕΙΝΑΝΔΡΑΣΠΕΛΟΠΟΝΝΗΣΙΟΥΣΟΤΙΠΛΕΙΣΤΟΥΣΚΑΙΒΕΛΤΙΣΤΟΥΣΩΣΕΠΙΒΟΥΛΕΥΟΝΤΟΣΤΙΣΣΑΦΕΡΝΟΥΣΤΑΙΣΠΟΛΕΣΙΚΑΙΓΑΡΗΣΑΝΑΙΙΩΝΙΚΑΙΠΟΛΕΙΣΤΙΣΣΑΦΕΡΝΟΥΣΤΟΑΡΧΑΙΟΝΕΚΒΑΣΙΛΕΩΣΔΕΔΟΜΕΝΑΙΤΟΤΕΔΕΑΦΕΙΣΤΗΚΕΣΑΝΠΡΟΣΚΥΡΟΝΠΑΣΑΙΠΛΗΝΜΙΛΗΤΟΥΕΝΜΙΛΗΤΩΙΔΕΤΙΣΣΑΦΕΡΝΗΣΠΡΟΑΙΣΘΟΜΕΝΟΣΤΑΑΥΤΑΤΑΥΤΑΒΟΥΛΕΥΟΜΕΝΟΥΣΑΠΟΣΤΗΝΑΙΠΡΟΣΚΥΡΟΝΤΟΥΣΜΕΝΑΥΤΩΝΑΠΕΚΤΕΙΝΕΤΟΥΣΔΕΞΕΒΑΛΕΝΟΔΕΚΥΡΟΣΥΠΟΛΑΒΩΝΤΟΥΣΦΕΥΓΟΝΤΑΣΣΥΛΛΕΞΑΣΣΤΡΑΤΕΥΜΑΕΠΟΛΙΟΡΚΕΙΜΙΛΗΤΟΝΚΑΙΚΑΤΑΓΗΝΚΑΙΚΑΤΑΘΑΛΑΤΤΑΝΚΑΙΕΠΕΙΡΑΤΟΚΑΤΑΓΕΙΝΤΟΥΣΕΚΠΕΠΤΩΚΟΤΑΣΚΑΙΑΥΤΗΑΥΑΛΛΗΠΡΟΦΑΣΙΣΗΝΑΥΤΩΙΤΟΥΑΘΡΟΙΖΕΙΝΣΤΡΑΤΕΥΜΑΠΡΟΣΔΕΒΑΣΙΛΕΑΠΕΜΠΩΝΗΞΙΟΥΑΔΕΛΦΟΣΩΝΑΥΤΟΥΔΟΘΗΝΑΙΟΙΤΑΥΤΑΣΤΑΣΠΟΛΕΙΣΜΑΛΛΟΝΗΤΙΣΣΑΦΕΡΝΗΝΑΡΧΕΙΝΑΥΤΩΝΚΑΙΗΜΗΤΗΡΣΥΝΕΠΡΑΤΤΕΝΑΥΤΩΙΤΑΥΤΑΩΣΤΕΒΑΣΙΛΕΥΣΤΗΝΜΕΝΠΡΟΣΕΑΥΤΟΝΕΠΙΒΟΥΛΗΝΟΥΚΗΙΣΘΑΝΕΤΟΤΙΣΣΑΦΕΡΝΕΙΔΕΝΟΜΙΖΕΠΟΛΕΜΟΥΝΤΑΑΥΤΟΝΑΜΦΙΤΑΣΤΡΑΤΕΥΜΑΤΑΔΑΠΑΝΑΝΩΣΤΕΟΥΔΕΝΗΧΘΕΤΟΑΥΤΩΝΠΟΛΕΜΟΥΝΤΩΝΚΑΙΓΑΡΟΚΥΡΟΣΑΠΕΠΕΜΠΕΤΟΥΣΓΙΓΝΟΜΕΝΟΥΣΔΑΣΜΟΥΣΒΑΣΙΛΕΙΕΚΤΩΝΠΟΛΕΩΝΩΝΤΙΣΣΑΦΕΡΝΟΥΣΕΤΥΓΧΑΝΕΝΕΧΩΝΑΛΛΟΔΕΣΤΡΑΤΕΥΜΑΑΥΤΩΙΣΥΝΕΛΕΓΕΤΟΕΝΧΕΡΡΟΝΗΣΩΙΤΗΙΚΑΤΑΝΤΙΠΕΡΑΣΑΒΥΔΟΥΤΟΝΔΕΤΟΝΤΡΟΠΟΝΚΛΕΑΡΧΟΣΛΑΚΕΔΑΙΜΟΝΙΟΣΦΥΓΑΣΗΝΤΟΥΤΩΙΣΥΓΓΕΝΟΜΕΝΟΣΟΚΥΡΟΣΗΓΑΣΘΗΤΕΑΥΤΟΝΚΑΙΔΙΔΩΣΙΝΑΥΤΩΙΜΥΡΙΟΥΣΔΑΡΕΙΚΟΥΣΟΔΕΛΑΒΩΝΤΟΧΡΥΣΙΟΝΣΤΡΑΤΕΥΜΑΣΥΝΕΛΕΞΕΝΑΠΟΤΟΥΤΩΝΤΩΝΧΡΗΜΑΤΩΝΚΑΙΕΠΟΛΕΜΕΙΕΚΧΕΡΡΟΝΗΣΟΥΟΡΜΩΜΕΝΟΣΤΟΙΣΘΡΑΙΞΙΤΟΙΣΥΠΕΡΕΛΛΗΣΠΟΝΤΟΝΟΙΚΟΥΣΙΚΑΙΩΦΕΛΕΙΤΟΥΣΕΛΛΗΝΑΣΩΣΤΕΚΑΙΧΡΗΜΑΤΑΣΥΝΕΒΑΛΛΟΝΤΟΑΥΤΩΙΕΙΣΤΗΝΤΡΟΦΗΝΤΩΝΣΤΡΑΤΙΩΤΩΝΑΙΕΛΛΗΣΠΟΝΤΙΑΚΑΙΠΟΛΕΙΣΕΚΟΥΣΑΙΤΟΥΤΟΔΑΥΟΥΤΩΤΡΕΦΟΜΕΝΟΝΕΛΑΝΘΑΝΕΝΑΥΤΩΙΤΟΣΤΡΑΤΕΥΜΑΑΡΙΣΤΙΠΠΟΣΔΕΟΘΕΤΤΑΛΟΣΞΕΝΟΣΩΝΕΤΥΓΧΑΝΕΝΑΥΤΩΙΚΑΙΠΙΕΖΟΜΕΝΟΣΥΠΟΤΩΝΟΙΚΟΙΑΝΤΙΣΤΑΣΙΩΤΩΝΕΡΧΕΤΑΙΠΡΟΣΤΟΝΚΥΡΟΝΚΑΙΑΙΤΕΙΑΥΤΟΝΕΙΣΔΙΣΧΙΛΙΟΥΣΞΕΝΟΥΣΚΑΙΤΡΙΩΝΜΗΝΩΝΜΙΣΘΟΝΩΣΟΥΤΩΣΠΕΡΙΓΕΝΟΜΕΝΟΣΑΝΤΩΝΑΝΤΙΣΤΑΣΙΩΤΩΝΟΔΕΚΥΡΟΣΔΙΔΩΣΙΝΑΥΤΩΙΕΙΣΤΕΤΡΑΚΙΣΧΙΛΙΟΥΣΚΑΙΕΞΜΗΝΩΝΜΙΣΘΟΝΚΑΙΔΕΙΤΑΙΑΥΤΟΥΜΗΠΡΟΣΘΕΝΚΑΤΑΛΥΣΑΙΠΡΟΣΤΟΥΣΑΝΤΙΣΤΑΣΙΩΤΑΣΠΡΙΝΑΝΑΥΤΩΙΣΥΜΒΟΥΛΕΥΣΗΤΑΙΟΥΤΩΔΕΑΥΤΟΕΝΘΕΤΤΑΛΙΑΙΕΛΑΝΘΑΝΕΝΑΥΤΩΙΤΡΕΦΟΜΕΝΟΝΣΤΡΑΤΕΥΜΑΠΡΟΞΕΝΟΝΔΕΤΟΝΒΟΙΩΤΙΟΝΞΕΝΟΝΟΝΤΑΕΚΕΛΕΥΣΕΛΑΒΟΝΤΑΑΝΔΡΑΣΟΤΙΠΛΕΙΣΤΟΥΣΠΑΡΑΓΕΝΕΣΘΑΙΩΣΕΣΠΙΣΙΔΑΣΒΟΥΛΟΜΕΝΟΣΣΤΡΑΤΕΥΕΣΘΑΙΩΣΠΡΑΓΜΑΤΑΠΑΡΕΧΟΝΤΩΝΤΩΝΠΙΣΙΔΩΝΤΗΙΕΑΥΤΟΥΧΩΡΑΙΣΟΦΑΙΝΕΤΟΝΔΕΤΟΝΣΤΥΜΦΑΛΙΟΝΚΑΙΣΩΚΡΑΤΗΝΤΟΝΑΧΑΙΟΝΞΕΝΟΥΣΟΝΤΑΣΚΑΙΤΟΥΤΟΥΣΕΚΕΛΕΥΣΕΝΑΝΔΡΑΣΛΑΒΟΝΤΑΣΕΛΘΕΙΝΟΤΙΠΛΕΙΣΤΟΥΣΩΣΠΟΛΕΜΗΣΩΝΤΙΣΣΑΦΕΡΝΕΙΣΥΝΤΟΙΣΦΥΓΑΣΙΤΟΙΣΜΙΛΗΣΙΩΝΚΑΙΕΠΟΙΟΥΝΟΥΤΩΣΟΥΤΟΙ
```
