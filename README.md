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

Versión básica
El sistema se basa en la idea de que dos interlocutores pueden generar conjuntamente una clave compartida sin que un intruso, que esté escuchando las comunicaciones, pueda llegar a obtenerla.

Para ello se eligen dos números públicos y, cada interlocutor, un número secreto. Usando una fórmula matemática, que incluye la exponenciación, cada interlocutor hace una serie de operaciones con los dos números públicos y su número secreto. A continuación los interlocutores se intercambian los resultados de forma pública. En teoría revertir esta función es tan difícil como calcular un logaritmo discreto (un sextillón de veces más costosa que la exponenciación usada para transformar los números). Por eso se dice que este número es el resultado de aplicar una función unidireccional al número secreto.

A continuación ambos interlocutores utilizan por separado una fórmula matemática que combina los dos números transformados con su número secreto y al final los dos llegan al mismo número resultado, que será la clave compartida.

https://github.com/11Feldman/EncryptedChat/blob/main/Diffie-Hellman-Schl%C3%BCsselaustausch.png

Descripción detallada

Diffie-Hellman.
Para dos partes Alice y Bob, que intentan establecer una clave secreta, y un adversario Mallory, la versión básica es como sigue:

Se establecen un primo {\displaystyle p}p y un generador {\displaystyle g\in \mathbf {Z} _{p}^{*}}g\in {\mathbf  {Z}}_{{p}}^{{*}} (3​). Estos son públicos, conocidos no solo por las partes Alice y Bob sino también por el adversario Mallory .
Alice escoge {\displaystyle a\in \mathbf {Z} _{p-1}}a\in {\mathbf  {Z}}_{{p-1}} al azar, calcula {\displaystyle A=g^{a}\;{\bmod {\;}}p}A=g^{{a}}\;{\bmod  \;}p, y envía {\displaystyle A}A a Bob
Bob escoge {\displaystyle b\in \mathbf {Z} _{p-1}}b\in {\mathbf  {Z}}_{{p-1}} al azar, calcula {\displaystyle B=g^{b}\;{\bmod {\;}}p}B=g^{{b}}\;{\bmod  \;}p, y envía {\displaystyle B}B a Alice
Nótese que tanto A como B pueden calcular el valor {\displaystyle K=g^{a\cdot b}\;{\bmod {\;}}p}K=g^{{a\cdot b}}\;{\bmod  \;}p. En efecto, lo podemos demostrar usando las propiedades del grupo {\displaystyle \mathbf {Z} _{p}^{*}}{\mathbf  {Z}}_{{p}}^{{*}}:

Para Alice: {\displaystyle B^{a}\;\;{\bmod {\;}}\;p=(g^{b}\;{\bmod {\;}}p)^{a}\;{\bmod {\;}}p=(\overbrace {(g^{b}\;{\bmod {\;}}p)(g^{b}\;{\bmod {\;}}p)\cdots (g^{b}\;{\bmod {\;}}p)} ^{a})\;{\bmod {\;}}p=g^{b\cdot a}\;{\bmod {\;}}p=g^{a\cdot b}\;{\bmod {\;}}p=K}B^{{a}}\;\;{\bmod  \;}\;p=(g^{b}\;{\bmod  \;}p)^{a}\;{\bmod  \;}p=(\overbrace {(g^{b}\;{\bmod  \;}p)(g^{b}\;{\bmod  \;}p)\cdots (g^{b}\;{\bmod  \;}p)}^{a})\;{\bmod  \;}p=g^{{b\cdot a}}\;{\bmod  \;}p=g^{{a\cdot b}}\;{\bmod  \;}p=K
Para Bob: {\displaystyle A^{b}\;{\bmod {\;}}p=(g^{a}\;{\bmod {\;}}p)^{b}\;{\bmod {\;}}p=(\overbrace {(g^{a}\;{\bmod {\;}}p)(g^{a}\;{\bmod {\;}}p)\cdots (g^{a}\;{\bmod {\;}}p)} ^{b})\;{\bmod {\;}}p=g^{a\cdot b}\;{\bmod {\;}}p=K}A^{{b}}\;{\bmod  \;}p=(g^{a}\;{\bmod  \;}p)^{b}\;{\bmod  \;}p=(\overbrace {(g^{a}\;{\bmod  \;}p)(g^{a}\;{\bmod  \;}p)\cdots (g^{a}\;{\bmod  \;}p)}^{b})\;{\bmod  \;}p=g^{{a\cdot b}}\;{\bmod  \;}p=K
Como ambas partes pueden calcular {\displaystyle K}K, entonces la podemos usar como clave compartida.
