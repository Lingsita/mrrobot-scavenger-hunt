# Generated by Django 3.1.2 on 2020-10-29 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_auto_20201027_0149'),
    ]

    operations = [
        migrations.RunSQL(
            """
            -- 2. Populate: path	
            insert into game_path(id, name, url_image) values (1, 'Path1', 'https://drive.google.com/file/d/16eUejNH5z181j6vvSieMYPkJWXyxybP8/view?usp=sharing');	
            insert into game_path(id, name, url_image) values (2, 'Path2', 'https://drive.google.com/file/d/1yLuhh4H_7VMEzNadBila_YhBFcVSoXgU/view?usp=sharing');	
            insert into game_path(id, name, url_image) values (3, 'Path3', 'https://drive.google.com/file/d/1H4rMoA_kjn5f4gluMzcCb1XoyZHSUyLf/view?usp=sharing');	
            insert into game_path(id, name, url_image) values (4, 'Path4', 'https://drive.google.com/file/d/1RtETLcn7Z65YESuXZkmhPaCoziYbBVf7/view?usp=sharing');	
            insert into game_path(id, name, url_image) values (5, 'Path5', 'https://drive.google.com/file/d/1FsIwbBH5pbwRTfZjYbpip5UTFhD21ZDg/view?usp=sharing');	
            insert into game_path(id, name, url_image) values (6, 'Path6', 'https://drive.google.com/file/d/1_8pnHmAHofsaRcHGUpmfUDOUNzvugFlr/view?usp=sharing');	
            insert into game_path(id, name, url_image) values (7, 'Path7', 'https://drive.google.com/file/d/12CreTEfe0GXbwU04Fe5LWwSLgUzOxCX9/view?usp=sharing');	
            insert into game_path(id, name, url_image) values (8, 'Path8', 'https://drive.google.com/file/d/1C9C-_NQmLqnK70grG7gbwpgQlbiNnO8X/view?usp=sharing');	
                
            -- 3. Populate: station	
            insert into game_station(id, name, place) values (1, 'DD0S.mpeg', 'Puente de madera');	
            insert into game_station(id, name, place) values (2, 'Rootk1t.mov', 'Rana - Esquina del camino de entrada');	
            insert into game_station(id, name, place) values (3, 'B4ckdoor.mkv', 'Lago: árbol pulpo y alrededores');	
            insert into game_station(id, name, place) values (4, 'R4nsomw4r3.qt', 'Palmera');	
            insert into game_station(id, name, place) values (5, 'Pr3text1ng.flv', 'Garaje');	
            insert into game_station(id, name, place) values (6, 'B41ting.wmv', 'Casa, piso 3');	
            insert into game_station(id, name, place) values (7, 'Ph1sh1ng.asf', 'Casa, piso 2');	
            insert into game_station(id, name, place) values (8, 'Da3m0n.m4v', 'Comedor interno');	
            insert into game_station(id, name, place) values (9, 'Hon3yp0t.avi', 'Arco - Símbolo π (mesa de piedra)');	
            insert into game_station(id, name, place) values (10, 'Expl01t.mp4', 'Zona BBQ');	
                
            -- 4. Populate: puzzle	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (1, 'Astrología (2P)','あデヅデでぎデ林デ ぎあфञデ', 'horoscopo chino', 'Alfabeto');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (2, 'No es arepa','Voy a comer _ _ _ _ _ paisa', 'arroz', 'CompletaLaFrase');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (3, 'Escritura','injak', 'kanji', 'Ordenar Letras');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (4, 'Programación','林うラあデञ', 'python', 'Alfabeto');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (5, 'Sistema','mnomoiscu', 'comunismo', 'Ordenar Letras');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (6, 'Guerreros','いキいヅぎфラデ ラいヅヅਡぎデラਡ', 'ejercito terracota', 'Alfabeto');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (7, 'Visual','El _ _ _ _ se usa para llamar la atención', 'rojo', 'CompletaLaFrase');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (8, 'Mitología','anrdog', 'dragon', 'Ordenar Letras');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (9, 'Arte (2P)','धゅञѠ Ѣゅ', 'kung fu', 'Alfabeto');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (10, 'Fenómeno','scaebloonropbi', 'sobrepoblacion', 'Ordenar Letras');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (11, 'Psicología','ラヅਡでラデヅञデ 林ਡヅਡञデфょい', 'trastorno paranoide', 'Alfabeto');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (12, 'Efímero','En el corazón, la vida. En la piel, el _ _ _ _ _ _.', 'tiempo', 'CompletaLaFrase');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (13, 'Cumpleañero','iocznah', 'chinazo', 'Ordenar Letras');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (14, 'Tecnología','百фਡデ円ф', 'xiaomi', 'Alfabeto');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (15, 'Deporte','pdiascraaa', 'paracaidas', 'Ordenar Letras');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (16, 'Tecnología','ぎфゃいヅでいѠゅヅфょਡょ', 'ciberseguridad', 'Alfabeto');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (17, 'Nooooo','Yo soy tú _ _ _ _ _.', 'padre', 'CompletaLaFrase');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (18, 'Enfermedad','iseiictapdn', 'apendicitis', 'Ordenar Letras');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (19, 'Tecnología','あゅਡщいф', 'huawei', 'Alfabeto');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (20, 'Idioma','diamnanr', 'mandarin', 'Ordenar Letras');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (21, 'Lugar','円ゅヅਡええਡ ぎあфञਡ', 'muralla china', 'Alfabeto');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (22, 'Obligación','Esa _ _ _ _ _ es una culebra que mata.', 'deuda', 'CompletaLaFrase');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (23, 'Juego','jedzera', 'ajedrez', 'Ordenar Letras');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (24, 'Actor (2P)','ゃヅゅぎい えいい', 'bruce lee', 'Alfabeto');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (25, 'Tencnología','mctoarpoud', 'computador', 'Ordenar Letras');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (26, 'Política (2P)','円ਡデ ラでい-ラゅञѠ', 'mao tse-tung', 'Alfabeto');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (27, 'Anime','Te voy a mostrar el 25% de mi máximo _ _ _ _ _.', 'poder', 'CompletaLaFrase');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (28, 'Actividad','oioescgn', 'negocios', 'Ordenar Letras');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (29, 'Ganador','фञѢфえラヅਡょデ', 'infiltrado', 'Alfabeto');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (30, 'Profesión','romadrgproa', 'programador', 'Ordenar Letras');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (31, 'Utensilio (2P)','林ਡえфええデで  ぎあфञデで', 'palillos chinos', 'Alfabeto');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (32, 'Revista','El _ _ _ _ _ _ es cochino, pero lo necesitamos.', 'dinero', 'CompletaLaFrase');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (33, 'Personaje','ぎфでぎデ', 'cisco', 'Alfabeto');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (34, 'Movimiento social','tissiaenrce', 'resistencia', 'Ordenar Letras');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (35, 'Héroe','キゅでラфぎфいヅデ', 'justiciero', 'Alfabeto');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (36, 'Retail (2P)','ਡえф  い百林ヅいでで', 'ali express', 'Alfabeto');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (37, 'Para ver estrellas','Los hongos, las _ _ _ _ _ _ más buscadas por Lili', 'drogas', 'CompletaLaFrase');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (38, 'Psicología','ਡえゅぎфञਡぎфデञ', 'alucinacion', 'Alfabeto');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (39, 'Fenómeno','octinmnaainoc', 'contaminacion', 'Ordenar Letras');	
            insert into game_puzzle (id, tip, description, answer, puzzle_type) values (40, 'Sistema','でデぎфいょਡょ', 'sociedad', 'Alfabeto');	
                
            -- 5. Populate: attack	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (1, '48fa9c1d-98d5-7df7-0466-d4146c26f291', 'Pinta con la boca', 'Dibuja un cerdito usando sólo la boca. Debes enviar selfie con el esfero en la boca y foto del resultado.', '2 Fotos');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (2, '8604f23d-de33-aa30-a34b-58d33d901f16', '¡A hacer ejercicio!', 'Haz una serie de ejercicio de 15 repeticiones. Puedes escoger entre flexiones de pecho, abdominales o sentadillas.', 'Video');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (3, '039b9409-14fc-f41e-eb9e-cc91fc6dc84e', 'Cerveza a fondo blanco', 'Destapa una cerveza y bebe todo su contenido a fondo blanco. Envía foto de la botella vacía.', 'Foto');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (4, 'ca8e6ccc-7fd2-90bb-4150-1b6f85f85fb9', 'Receta creativa', 'Ve a la cocina y toma 4 productos al azar (el agua no cuenta). Revuélvelos y bebe la mezcla sin escupir. Debes grabar el proceso de la mezcla hasta la bebida.', 'Video');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (5, '159cbd3f-bbdf-ac5b-e1e2-40ecc4202a9b', 'Concentración numérica con números prohibidos', 'Di, al revés, los números del 30 al 1, pero sin mencionar los múltiplos de 3. Si te equivocas, vuelve a empezar hasta que lo digas todo bien.', 'Video');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (6, '437d961a-22de-9c00-de9b-1dfa44fe9126', 'Pinta con la boca', 'Dibuja un cerdito usando sólo la boca. Debes enviar selfie con el esfero en la boca y foto del resultado.', '2 Fotos');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (7, 'dc799520-3d66-ee46-e72e-8a0cab6f57d8', '¡A hacer ejercicio!', 'Haz una serie de ejercicio de 15 repeticiones. Puedes escoger entre flexiones de pecho, abdominales o sentadillas.', 'Video');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (8, '070d9b17-9526-4830-b51d-573505d9957b', 'Cerveza a fondo blanco', 'Destapa una cerveza y bebe todo su contenido a fondo blanco. Envía foto de la botella vacía.', 'Foto');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (9, 'b3b2130b-1c74-56dd-b221-4dae2a9a9e7a', 'Difícil de arrastrar', 'Arrástrate por el piso sentado sin usar las manos. Debes cubrir una distancia mínima de 1 metro en línea recta.', 'Video');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (10, 'e112b11d-b15d-30f3-d1f4-2f6b215b0edb', 'Encholar el ping pong', 'Mueve un ping pong mediante soplidos usando los cilindros de cartón. El ping pong debe ir de un extremo del comedor hasta el otro extremo y ser encholado en el vaso. No puedes usar las manos.', 'Video');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (11, 'b38b7b7b-2597-c95b-76ea-f34011daef65', 'Pinta con la boca', 'Dibuja un cerdito usando sólo la boca. Debes enviar selfie con el esfero en la boca y foto del resultado.', '2 Fotos');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (12, '79ac2b0f-372f-40cb-65c1-0d8fd1953acb', '¡A hacer ejercicio!', 'Haz una serie de ejercicio de 15 repeticiones. Puedes escoger entre flexiones de pecho, abdominales o sentadillas.', 'Video');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (13, 'e8f82f74-2b4a-ca9a-0721-fc96f1a0f5a9', 'Cerveza a fondo blanco', 'Destapa una cerveza y bebe todo su contenido a fondo blanco. Envía foto de la botella vacía.', 'Foto');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (14, 'fda7a534-8fa5-209f-7e8f-04507f6ccf22', 'Habilidad dando giros', 'En el pasto al lado del camino de la casa a la piscina, debes dar giros, rollos o "vuelta canela" hasta terminar el camino.', 'Video');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (15, '6ccc949b-1a50-3c18-f641-499e2ee467cf', 'Búsqueda harinosa', 'En el recipiente con harina hay un objeto que debes sacar con la boca. NO se pueden utilizar las manos.  Envía video del proceso y foto cuando atrapes el objeto. La selfie debe ser con el objeto en la boca.', '1 Foto y 1 Video');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (16, 'c2d0b327-481a-fabe-2750-b1368e653b13', 'Pinta con la boca', 'Dibuja un cerdito usando sólo la boca. Debes enviar selfie con el esfero en la boca y foto del resultado.', '2 Fotos');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (17, 'f58767af-893b-c4e5-9552-1f5ec40b2c77', '¡A hacer ejercicio!', 'Haz una serie de ejercicio de 15 repeticiones. Puedes escoger entre flexiones de pecho, abdominales o sentadillas.', 'Video');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (18, '0920dc16-1ab4-0dc2-065e-7ff3ea7fe329', 'Cerveza a fondo blanco', 'Destapa una cerveza y bebe todo su contenido a fondo blanco. Envía foto de la botella vacía.', 'Foto');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (19, '8a650a04-36ed-3cf8-7fcb-d196c77d3be5', 'Trabalengüas', 'Di el siguiente trabalengüas sin equivocarte: «Tengo una gallina pinta, pipiripinta, pipirialegre y gorda, que tiene tres pollitos pintos, pipiripintos, pipirialegres y gordos. Si la gallina no hubiera sido pinta pipiripinta, pipirialegre y gorda; los pollitos no hubieran sido pintos, pipiripintos, pipirialegres y gordos.»', 'Video');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (20, 'c2d8f317-ec04-0483-046e-6ea647af2d41', 'Ráfaga de masmelos', 'Llena tu boca con 12 masmelos y aún con ellos en la boca, tómate una selfie.', 'Foto');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (21, '40a366b3-0956-e40c-670f-fa873f6d7f5a', 'Escribe con los pies', 'Escribe tu primer o segundo nombre completo usando los pies. Envía 1 foto de cuerpo entero usando el esfero con el pie (NO selfie), y otra con el resultado.', '2 Fotos');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (22, '89f8b139-6f24-a675-e83c-8ff9206988cb', '¡A hacer ejercicio!', 'Haz una serie de ejercicio de 15 repeticiones. Puedes escoger entre flexiones de pecho, abdominales o sentadillas.', 'Video');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (23, '0c53d217-558a-40cc-66ce-78781c7c660c', 'Cerveza a fondo blanco', 'Destapa una cerveza y bebe todo su contenido a fondo blanco. Envía foto de la botella vacía.', 'Foto');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (24, '5a2ab86b-2bca-e6cd-810d-99b6b72e4dfa', 'Ponerle picante a la vida', 'Toma una cucharada de picante y saboréala por un instante. Luego la puedes escupir, y tomar el agua que quieras.', 'Video');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (25, 'e215a3c6-59b6-00aa-e687-cf6872108164', 'Rapidez alfabética', 'Tienes que decir el alfabeto al revés. Si te equivocas, deberás volver a empezar.', 'Video');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (26, 'ac0a0300-fc16-a6cf-4cdd-dc9085970e7c', 'Escribe con los pies', 'Escribe tu primer o segundo nombre completo usando los pies. Envía 1 foto de cuerpo entero usando el esfero con el pie (NO selfie), y otra con el resultado.', '2 Fotos');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (27, '5bf13698-f2cf-fbce-3a77-3885aa1187b3', '¡A hacer ejercicio!', 'Haz una serie de ejercicio de 15 repeticiones. Puedes escoger entre flexiones de pecho, abdominales o sentadillas.', 'Video');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (28, '19959b97-45b2-ef15-307e-e5690b49fe95', 'Cerveza a fondo blanco', 'Destapa una cerveza y bebe todo su contenido a fondo blanco. Envía foto de la botella vacía.', 'Foto');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (29, '58f24768-3911-c615-2fae-5b9027117bfe', 'Mascarilla frutal', 'Haz una mascarilla con el banano y aplícatela. Debes cubrir todo el rostro, excepto los ojos, por supuesto!', 'Foto');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (30, 'e684bd90-f740-6fbc-3c53-42cbb29a9660', 'Canto complicado', 'Cantar una canción cualquiera mientras te comes tres galletas secas, sin agua.', 'Video');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (31, '2d01f7c0-b664-c72b-f32b-92bc902dd6cb', 'Escribe con los pies', 'Escribe tu primer o segundo nombre completo usando los pies. Envía 1 foto de cuerpo entero usando el esfero con el pie (NO selfie), y otra con el resultado.', '2 Fotos');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (32, '69aadf91-313d-b49d-2220-2e8ae99aff34', '¡A hacer ejercicio!', 'Haz una serie de ejercicio de 15 repeticiones. Puedes escoger entre flexiones de pecho, abdominales o sentadillas.', 'Video');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (33, 'c2bf2182-e474-7be1-5145-861583abbb8a', 'Cerveza a fondo blanco', 'Destapa una cerveza y bebe todo su contenido a fondo blanco. Envía foto de la botella vacía.', 'Foto');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (34, 'd2d40704-bfc0-05c3-1da8-5b90a8498f41', 'Peluca creativa', 'Recolecta los materiales a tu alcance para hacer una peluca creativa: hojas de árbol, papeles, cordones... lo que se te ocurra. Ponte la peluca y envía la selfie correspondiente.', 'Foto');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (35, '1b051ae8-aa60-6b07-b2b0-fe6131c7d48a', 'Nos pusimos románticos', 'Busca cualquier poema en internet y recítalo como si se lo estuvieras dedicando a alguien y le tuvieras en frente.', 'Video');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (36, '18682cf2-9568-123a-8475-6e570460f288', 'Escribe con los pies', 'Escribe tu primer o segundo nombre completo usando los pies. Envía 1 foto de cuerpo entero usando el esfero con el pie (NO selfie), y otra con el resultado.', '2 Fotos');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (37, 'e7516ff9-38fd-bdd9-a330-28d3fe3131d8', '¡A hacer ejercicio!', 'Haz una serie de ejercicio de 15 repeticiones. Puedes escoger entre flexiones de pecho, abdominales o sentadillas.', 'Video');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (38, 'be55666f-b740-1e04-0d08-ee615461443e', 'Cerveza a fondo blanco', 'Destapa una cerveza y bebe todo su contenido a fondo blanco. Envía foto de la botella vacía.', 'Foto');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (39, '865229c7-7d00-36b2-56d3-78900fd99df6', 'Modelado con plastilina', 'Con plastilina de diferentes colores, haz una moto y una persona montada en ella, simulando que la moto está en movimiento, es decir, la persona va manejando. Recuerda que el casco es obligatorio.', 'Foto');	
            insert into game_attack (id, attack_uuid, title, description, evidence_type) VALUES (40, '006a787b-ac7c-f6b7-af39-ca98f7c31793', 'Rimas a la carrera', 'Debes componer por lo menos 2 rimas cortas, de dos frases o versos, usando las palabras "paseo" y "bosque".  Ejemplo con "camisa" y "zapato":  «Mi mamá me regaló una CAMISA, con la que siempre voy a misa. Mi papá se quitó un ZAPATO y empezó a oler a gato.»', 'Video');	
                
            -- 6. Populate: step	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (1, 1, 1, 2, 1, 1);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (2, 1, 2, 3, 2, 2);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (3, 1, 3, 5, 3, 3);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (4, 1, 4, 7, 4, 4);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (5, 1, 5, 9, 5, 5);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (6, 2, 1, 1, 6, 6);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (7, 2, 2, 2, 7, 7);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (8, 2, 3, 4, 8, 8);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (9, 2, 4, 6, 9, 9);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (10, 2, 5, 9, 10, 10);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (11, 3, 1, 1, 11, 11);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (12, 3, 2, 3, 12, 12);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (13, 3, 3, 7, 13, 13);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (14, 3, 4, 8, 14, 14);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (15, 3, 5, 10, 15, 15);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (16, 4, 1, 1, 16, 16);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (17, 4, 2, 4, 17, 17);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (18, 4, 3, 6, 18, 18);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (19, 4, 4, 8, 19, 19);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (20, 4, 5, 10, 20, 20);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (21, 5, 1, 1, 21, 21);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (22, 5, 2, 2, 22, 22);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (23, 5, 3, 3, 23, 23);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (24, 5, 4, 5, 24, 24);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (25, 5, 5, 7, 25, 25);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (26, 6, 1, 2, 26, 26);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (27, 6, 2, 4, 27, 27);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (28, 6, 3, 6, 28, 28);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (29, 6, 4, 8, 29, 29);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (30, 6, 5, 9, 30, 30);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (31, 7, 1, 4, 31, 31);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (32, 7, 2, 5, 32, 32);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (33, 7, 3, 7, 33, 33);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (34, 7, 4, 9, 34, 34);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (35, 7, 5, 10, 35, 35);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (36, 8, 1, 3, 36, 36);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (37, 8, 2, 5, 37, 37);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (38, 8, 3, 6, 38, 38);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (39, 8, 4, 8, 39, 39);	
            insert into game_step(id, path_id, "order", station_id, puzzle_id, attack_id) VALUES (40, 8, 5, 10, 40, 40);	
            """)
    ]
