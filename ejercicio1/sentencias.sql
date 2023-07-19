SELECT id FROM usuarios WHERE name= 'Juan';

INSERT INTO usuarios (`id`,`nombre`,`apellido`,`mail`) VALUES (NULL,'Jesus','RV','jesus@rv.com');

UPDATE usuarios SET edad = 60 WHERE nombre='Juan';
