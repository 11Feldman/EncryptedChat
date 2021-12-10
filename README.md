# Chat Encriptado
Chat encriptado con protocolo Diffie Hellman en python.

# Diffie-Hellman
El protocolo criptográfico Diffie-Hellman, debido a Whitfield Diffie y Martin Hellman (autores también del problema de Diffie-Hellman o DHP), es un protocolo de establecimiento 
de claves entre partes que no han tenido contacto previo, utilizando un canal inseguro y de manera anónima (no autenticada).
Se emplea generalmente como medio para acordar claves simétricas que serán empleadas para el cifrado de una sesión (establecer clave de sesión). 
Siendo no autenticado, sin embargo, provee las bases para varios protocolos autenticados.

Su seguridad radica en la extrema dificultad (conjeturada, no demostrada) de calcular logaritmos discretos en un cuerpo finito.

Whitfield Diffie y Martin Hellman recibieron el prestigioso premio A.M. Turing de 2015 de la Association for Computer Machinery en 2016 por este trabajo 
"que revolucionó la seguridad informática".

## Versión básica
El sistema se basa en la idea de que dos interlocutores pueden generar conjuntamente una clave compartida sin que un intruso, que esté escuchando las comunicaciones, pueda llegar a obtenerla.
Para ello se eligen dos números públicos y, cada interlocutor, un número secreto. Usando una fórmula matemática, que incluye la exponenciación, cada interlocutor hace una serie de operaciones con los dos números públicos y su número secreto. A continuación los interlocutores se intercambian los resultados de forma pública. En teoría revertir esta función es tan difícil como calcular un logaritmo discreto (un sextillón de veces más costosa que la exponenciación usada para transformar los números). Por eso se dice que este número es el resultado de aplicar una función unidireccional al número secreto.

A continuación ambos interlocutores utilizan por separado una fórmula matemática que combina los dos números transformados con su número secreto y al final los dos llegan al mismo número resultado, que será la clave compartida.

![Diffie-Hellman-Schlüsselaustausch](https://user-images.githubusercontent.com/44484762/145516693-f169148d-30c3-4514-9a6b-7934aa4d04fd.png)


Wikipedia: [Diffie-Hellman](https://es.wikipedia.org/wiki/Diffie-Hellman)

# Funcionamiento aplicacion
___
Para poder realizar la prueba puede copiar el repositorio con el siguiente codigo

git clone 
