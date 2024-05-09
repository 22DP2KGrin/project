# Grupu pārvaldības lietotne 

  

## Pārskats 

  

Grupu pārvaldības lietotne ir Python aplikācija, kas izveidota, izmantojot Tkinter bibliotēku. Tā kalpo kā pārvaldības rīks lietotāju kontiem un grupām. Lietotāji var reģistrēties, ieiet sistēmā, izveidot savas piezīmes par filmu vai seriālu, kuru lietotājs grib apskatīt, rediģēt piezīmes, dzēst tos, pārnest savas piezīmes divās dažādās mapēs . 

  

## Iespējas 

  

- **Lietotāju autentifikācija:** Lietotāji var reģistrēties ar lietotājvārdu un paroli vai pierakstīties sistēmā, izmantojot esošos autentifikācijas datus. 

- **Piezīmes izveidošanas:** Lietotāji var izveidot savu piezīmi, uzrakstīt tām nosaukumu, aprakstu un izvelētos mapi, kurā lietotājs grib ievietot savu piezīmi. 

- **Piezīmes rediģēšana:** Lietotājs var arī rediģēt savas piezīmes, kā arī rediģēt mapi, kurā tā piezīme glābsies. 

  

## Lietotne tiek izmantota: 

  

- `Tkinter`: GUI izveidei. 

- `sqlite3`: Datiem saglabāšanai un nolasīšanai SQLite datu bāzē. 

- `threading`: Datu bāzes darbību izpildei atsevišķā pavedienā. 

  

## Kā lietot 

  

1. **Instalācija:** 

   Pārliecinieties, ka jums ir uzstādīts Python sistēmā. 

   Papildu instalācija nav nepieciešama, jo lietojot izmanto standarta Python bibliotēkas. 

  

2. **Lietotnes palaišana:** 

   Izpildiet Python kodu, ko nodrošinājām. 

  

3. **Lietotāju reģistrācija/pierakstīšanās:** 

   Lietotāji var reģistrēties ar lietotājvārdu un paroli vai pierakstīties sistēmā, izmantojot esošos autentifikācijas datus. 

  

4. **Piezīmes izveidošana:** 

   Lietotāji var izveidot sev piezīmes ar filmas un seriālus nosaukumiem, ka arī pilnveidot tos ar personīgo aprakstu. 

  

5. **Piezīmes rediģēšana:** 

 Pēc vajadzības lietotājs var rediģēt savas pašas piezīmes un to saturu, ka arī tos atrašanas vietas.  

  

## Datu saglabāšana 

  

Lietotnes dati tiek saglabāti SQLite datu bāzē (`example.db`). 

  

## Nākotnes uzlabojumi 

  

- Lietotāju profili. Katram lietotājam būs savs profils, kurā var pievienot profila foto, izveidot profila aprakstu.  

- Integrāciju ar filmu datu bāzēm. Lietotājam nebūs vajadzīgs pašam rakstīt filmas vai seriālus, būs pietiekami atrast nosaukumu un datu bāzē jau būs visa informācija par to. 

- Draugu saraksts. Lietotājs varēs lietotnē pievienot draugus draugu sarakstā, lai abi lietotāji varētu sazināties un dalīties ar filmām viens ar otru.   

 

 
