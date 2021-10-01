# ESTRUTURAS DE REPETIÇÃO

Às vezes, é comum que precisemos que uma mesma instrução (ou um conjunto de instrução) precise ser executada várias vezes seguidas. 
Nesses casos, normalmente utilizamos um loop (ou laço de repetição). Essas estruturas nos permitem executar o mesmo bloco de código até que uma condição, passada como parâmetro, seja satisfeita.
Abaixo são descritas as duas principais estruturas de repetição que utilizamos na linguagem Python.

## 1) ESTRUTURA ```FOR```
Em algumas linguagens de programação, como o C, o ```for``` utilizado geralmente com uma variável do tipo inteiro que funciona como um índice, controlando a quantidade de vezes que a interação do bloco será realizada.
Em C, por exemplo, é comum que escrevamos algo do tipo: 


```c
for (i = 0; i < 10; i++) {
 printf("%d", &i)
}
```

O laço ```for``` em Python nos permite percorrer os itens de uma coleção e, para cada um deles, executar o bloco de código declarado no loop. Sua sintaxe é a seguinte:

```python
for <item> in <conjunto_de_itens>:
    <quero_que_voce_faca_isso_ok>
```

Enquanto percorremos esse conjunto de itens, a variável indicada no for receberá, a cada iteração, um item dessa coleção.
Vamos supor que você tem a seguinte lista com seus professores favoritos do curso de computação: 

```python
professores = ['Ricardo', 'Rosalvo', 'Marcus']
```

Pedimos, então, para o laço ```for``` printar cada item dessa lista utilizando o exemplo abaixo:

```python
for n in professores:
     print(n + " <3")
```

### 1.1) BREAK
É possível modificar a condição do laço ```for``` e interromper o loop no meio do caminho. 
Para isso, utilizamos a instrução ```break```, que encerra a execução do loop ao encontrar uma condição específica. O ```break``` geralmente está associado ao uso do condicional ```if``` dentro do laço de repetição. Por exemplo:

```python
professores = ['Ricardo', 'Rosalvo', 'Marcus']

for n in professores:
     print(n + " <3")
     if n == 'Ricardo':
        print("Ricardo é o professor mais lindo!!!!!!")
        break
```



Devemos utilizar a instrução break em conjunto com uma estrutura condicional, como a if/else ou até mesmo com outro laço de repetição for. Veja como fica a sintaxe da estrutura de repetição quando utilizamos o break:

### 1.2) FOR/ELSE
É possível também acrescentar a instrução ```else``` diretamente no final da estrutura for. 
Isso faz com que um novo bloco de código seja executado AO FINAL de todas as iterações do ```for```. Por exemplo:

```python
professores = ['Ricardo', 'Rosalvo', 'Marcus']

for n in professores:
     print(n + " <3")
else:
     print("Não existem mais outros professores além desses.")
```

Podemos descrever esse exemplo linha por linha: 
<ul> 
<li> Na primeira linha, definimos uma variável que armazenará uma lista de nomes. 
<li> O laço for percorre todos esses itens, atribuindo-os à variável n, que será impressa e exibirá os nomes um-a-um.
<li> Após o fim do loop, a instrução else é chamada, imprimindo a declarada a seguir.
</ul>




## 2) ESTRUTURA ```WHILE```

Enquanto o comando ```for``` executa o laço de repetição até que a condição seja atendida, o comando while faz com que um conjunto de instruções seja executado <i>enquanto</i> uma condição é atendida. Quando o resultado dessa condição passa a ser falso, a execução do loop é interrompida, como mostra o exemplo a seguir:

```python
contador = 0
while (contador < 5):
       print(contador)
       contador = contador + 1
```

Podemos ler esse trecho de código da seguinte forma: um contador, iniciando a partir do 0, é chamado. O laço ```while``` primeiramente vai conferir se esse valor é menor que 5; caso seja, ele exibirá esse valor na tela e, em seguida, somará mais um ao contador. Dessa forma, vai existir um momento em que esse contador se igualará a 5 e, portanto, o laço ```while``` vai parar de executar o bloco de comandos abaixo dele. Lembrando que <i>em Python, para indicar o bloco de código pertencente ao while, devemos apenas indentar o código, conforme demonstrado no exemplo.</i> 


### 2.1) WHILE/ELSE
Assim como no ```for```, também é possível a instrução ```else``` à execução do ```while```. O propósito disso tambem é executar algum bloco de instruções ao finalizar o laço de repetição. 

```python
contador = 0
while (contador < 5):
      print(contador)
      contador = contador + 1
else:
      print("[Galvão Bueno's voice] É PENTAAAAAAA, É PENTAAAAAAAA")
```

## FIXANDO O APRENDIZADO.
Já sente confiança para praticar? Faça a lista de exercícios clicando <a href="https://github.com/edjairaguiar/minicurso-python/blob/main/exercicios/lista3.md">aqui</a>.
