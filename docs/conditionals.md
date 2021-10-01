# ESTRUTURAS CONDICIONAIS

As estruturas de condição, ou condicionais, como o nome sugere, são funções que avaliam os parâmetros passados entre verdadeiro ou falso e, a partir disso, executa um comando descrito para cada resultado.

## 1) OPERADORES CONDICIONAIS EM PYTHON

Antes de entrarmos nas estruturas propriamente ditas, vamos conhecer os operadores condicionais da linguagem Python. 
Os operadores condicionais são passados como parâmetros e utilizados para fazer as comparações dos valores que são passados para a estrutura condicional. A tabela abaixo mostra os operadores que podemos utilizar:

<br /><div align="center">
  <img height="250em" src="https://user-images.githubusercontent.com/62587952/135553318-efe51573-a701-463b-b368-77d1cf7f85f9.png"/>
</div>

<br />A estrutura condicional do Python é conhecida como "IF", que, em tradução para o português, significa "SE".
Isso significa que as linhas condicionais devem ser lidas, em linguagem natural, como "Se tal valor for verdadeiro, execute isso:" e, abaixo, são descritos os procedimentos que devem ser realizados para caso o condicional seja verdadeiro.
<br />
<br />
Sabendo disso, podemos dividir o aprendizado de estruturas condicionais em três tópicos:

### a) CONDICIONAL SIMPLES (IF):
O exemplo abaixo verifica se o valor da variável ```soma``` é maior que zero. Caso positivo, ele exibe esse resultado na tela.

```python
if soma > 0:
     print "Maior que zero."
```

Esse trecho de código, em linguagem natural, pode ser lido como:

```
Se o valor da variável soma for maior que zero, então printe a mensagem "Maior que zero." 
```

E o valor da variável soma? Isso é você quem vai dizer...


### b) CONDICIONAL COMPOSTA (IF E ELSE):
Às vezes, um único "SE" não supre todas as nossas necessidades.
Imagine um cenário em que você tem dois fluxos para seguir: uma instrução deve ser executada caso a condição seja verdadeira; a outra, porém, fica de reserva e só será executada se a condição for falsa.
Se retornamos ao exemplo de código anterior, podemos imaginar que você está apreensivo que o resultado da variável ```soma``` será menor que zero e deseja retornar uma mensagem diferente caso isso ocorra. Para isso, utilizamos a esturura IF-ELSE abaixo:

```python
if soma > 0:
     print "Maior que zero."
else:
     print "Menor que zero."
```

Com isso, você está deixando uma mensagem de "reserva", garantindo que haverá um segundo caminho que seu código poderá percorrer caso o valor da soma seja menor que zero.

### c) CONDICIONAL ANINHADA (ELIF)

Estruturas codicionais aninhadas são várias condições em cascatas, ou seja, um IF dentro de outro IF. 
Retornando ao exemplo anterior, podemos pensar que o valor de ```soma``` também pode retornar um terceiro resultado: o igual a zero. Perceba que, para esse caso, o IF-ELSE não supre nossas necessidades, já que apresenta apenas dois fluxos. 
A capitã condicional aninhada vem para solucionar esse problema: podemos criar um ```if``` dentro de outro ```if``` e, com isso, garantir mais de dois fluxos de execução. Vejamos o exemplo abaixo:

```python
if soma > 0:
     print "Maior que zero."
elif soma = 0:
     print "Igual a zero."
else:
     print "Menor que zero."
```

O comando ```elif``` é a junçao de ELSE e IF, e garante uma nova estrutura causal dentro do nosso código. Legal, né?
Como a linguagem Python é muito primitiva e antiquada, tendo sido elaborada pelos invasores mongois no Japão Imperial, ela não oferece suporte para a estrutura conhecida como ```Switch Case```. Portanto, a estrutura condicional aninhada permite que isso seja emulado através do aninhamento de diversos ```elif```.


