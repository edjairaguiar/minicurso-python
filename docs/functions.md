<h2>1) MÓDULOS</h2>

Módulos são arquivos de código Python com a extensão .py, que podem ser importados por
outros módulos.
A modularização de um programa é algo bastante importante por duas razões principais:
<li> É possível reutilizar o código escrito em outras aplicações;
<li> Estando o código do programa organizado, temos maior facilidade no controle e no
entendimento da aplicação;

Quando importamos um módulo para nosso código, as declarações do arquivo importado (suas
variáveis, suas funções e etc.) ficam disponíveis para serem usadas. É mais ou menos como a
importação de uma biblioteca na linguagem .C, por exemplo.

Nós chamamos um módulo no nosso programa utilizando a linha de comando

```$ import nomeDoMódulo```

A extensão .py deve ser omitida.

<h2>2) CRIANDO E ACESSANDO ATRIBUTOS DE MÓDULOS</h2>

Cada módulo tem suas próprias declarações de variáveis, funções, classes... cada uma delas carrega com si seu nome. Podemos acessar as variáveis e funções do módulo no nosso programa. Para isso, utilizamos a notação

```$ nomeDoMódulo.nomeDaFuncao```

EXEMPLO: Podemos abrir o editor de texto e escrever uma função simples como na Figura 1. Salvamos o nome do arquivo como teste.py.

<div align="center">
  <img height="150em" src="../img/functions/fig1.png"/>
  <h6>Figura 1 – Código do módulo teste.py</h6>
</div>

[!] ATENÇÃO: Salve o arquivo do módulo em uma pasta fácil de acessar, pois antes de chamar o interpretador python precisaremos acessar a pasta pelo prompt de comando. Eu salvei na pasta Documentos. Dessa forma, primeiro acessei a pasta onde salvei o arquivo e só então chamei o interpretador python, como visto na Figura 2.

<div align="center">
  <img height="150em" src="../img/functions/fig2.png"/>
  <h6>Figura 2 – Precisamos acessar a pasta onde o arquivo foi salvo antes de chamar o python</h6>
</div>

Agora que salvamos nosso módulo, vamos chamá-lo para nosso programa, escrevendo ```import teste```. Logo em seguida, chamamos nossa função f digitando ```teste.f()```. O resultado podemos ver na Figura 3.

<div align="center">
  <img height="150em" src="../img/functions/fig3.png"/>
  <h6>Figura 3– Chamamos a função f() através do módulo teste.py</h6>
</div>

<h2>3) MÓDULOS PADRÕES</h2>
O Python traz uma biblioteca padrão de módulos, embutidas no interpretador da linguagem. Esses módulos permitem o acesso a algumas operações que não fazem parte do núcleo da linguagem, mas estão no interpretador por eficiência.

Por exemplo: funções matemáticas não estão tradicionalmente inclusas no escopo de funções de entrada e saída da linguagem. Nesse caso, temos duas opções: implementá-las manualmente; ou importar o módulo math, que disponibiliza grande parte das funções matemáticas que conhecemos na calculadora científica.


<div align="center">
  <table>
    <tr>
    <td>math.exp(x)</td>
    <td>𝑒𝑥</td>
    </tr>
    <tr>
    <td>math.log10(x)</td>
    <td>Logaritmo do parâmetro x na base 10</td>  
    </tr>
    <tr>
    <td>math.pow(x, y)</td>
    <td>𝑥^𝑦</td>  
    </tr>
    <tr>
    <td>math.sqrt(x</td>
    <td>√𝑥</td>  
    </tr>
    <tr>
    <td>math.degrees(x)</td>
    <td>Converte x radianos para graus</td> 
    </tr>
    <tr>
    <td>math.radians(x)</td>
    <td>Converte x graus para radianos</td>
    </tr>
  </table>
  <h6>Tabela 1 – Algumas funções do módulo math</h6>
</div>

Na Figura 4 temos um exemplo da utilização do módulo math, utilizando a função ```math.sqrt()```.

<div align="center">
  <img height="150em" src="../img/functions/fig4.png"/>
  <h6>Figura 4 – Cálculo de raiz quadrada com função math.sqrt</h6>
</div>

<h2>4) OBSERVAÇÕES</h2>
<li>O editor de texto usado é o Visual Studio Code. Entretanto é possível utilizar qualquer outro editor de texto, desde que a extensão do arquivo seja salva como .py. Outro editores de texto que podem ser usados: WordPad, Notepad++.
<li>A importação de módulos é custosa computacionalmente, portanto o Python só a realiza uma vez. Caso editemos o módulo durante a execução do nosso código e precisemos que a edição seja utilizada, podemos forçar que o módulo seja importado novamente usando o comando reload(nomeDoMódulo).
  
<h2>5) ARQUIVOS PYTHON</h2>
Embora a opção de utilizar o modo interativo seja uma boa forma de aprender e praticar a sintaxe da linguagem Python, concordemos que não é a forma mais elegante de programar e rodar nossas aplicações.

Assim como em qualquer outra linguagem, é muito mais prático que rodemos nossos programas quando já estão finalizados, em formato de arquivo. Podemos utilizar uma IDE (como usamos o DEV ou o CodeBlocks para programar em .C, por exemplo), mas sempre existe a opção de primeiramente escrever o programa completo em um editor de texto e em seguida executá-lo no prompt de comando.

Por enquanto utilizaremos a opção de executar arquivos no prompt de comando, pois os ambientes de desenvolvimento Python serão abordados mais futuramente, em um capítulo à parte. 

<h3>5.1) Executando arquivos .py</h3>
Assim como os módulos, a extensão de arquivo dos nossos códigos é .py. Vamos escrever um programa simples. Podemos abrir o editor de texto e escrever um programa para simplesmente exibir uma saudação na tela e se despedir quando o usuário digitar qualquer coisa no teclado, como na Figura 5.

<div align="center">
  <img height="150em" src="../img/functions/fig5.png"/>
  <h6>Figura 5 – Arquivo contendo um programa simples em Python.</h6>
</div>
  
Salvamos nosso arquivo com o nome hellobye.py
  
Se você já configurou o interpretador Python seu prompt de comando, agora basta especificar o caminho do seu arquivo no prompt. Isso mesmo: não há necessidade de chamar o interpretador digitando python. Simplesmente especifique o caminho do arquivo no seu promp de comando e o seu arquivo irá executar.

[!] DICA: se você ficar com preguiça de digitar o caminho do arquivo, pode simplesmente arrastá-lo para o prompt e ele reconhecerá o caminho automaticamente
  
Quando o caminho do arquivo estiver especificado no prompt, basta teclar enter e o código será executado, sem maiores problemas.

<div align="center">
  <img height="150em" src="../img/functions/fig6.png"/>
  <h6>Figura 6 – O código é executado em sua completude, sem necessidade de digitar comandos linha por linha no prompt. Muito mais elegante.</h6>
</div>
  
<h3>5.2) Importando módulos em arquivos de código</h3>
<h4>5.2.1) Módulos padrões</h4>
Para acessarmos módulos padrões de Python dentro dos nossos arquivos de código, ao invés de os chamarmos no prompt, devemos declará-los no cabeçalho do código, da mesma forma que as bibliotecas em linguagem C. Por exemplo: suponhamos o código da Figura 3, que calcula a raiz quadrada de um número que o usuário insere.

<div align="center">
  <img height="150em" src="../img/functions/fig7.png"/>
  <h6>Figura 7 – Programa para calcular raiz quadrada. Observe que o import precisou ser chamado no início do script.</h6>
</div>
  
[1] LEMBRE-SE: A função input() deve ser usada dentro da função conversão int(). Lembra da primeira aula? O input lê a entrada do usuário como uma string, mas precisamos que a entrada seja um inteiro para operar a raiz quadrada. 
[2] LEMBRE-SE: Para acessarmos as funções que existem em um módulo, precisamos especificar de qual módulo está vindo a função, no formato ```nomeDoMódulo.nomeDaFunção()```.
  
Agora podemos simplesmente chamar nosso programa no prompt de comando e executá-lo.

<div align="center">
  <img height="150em" src="../img/functions/fig8.png"/>
  <h6>Figura 8 – Execução do código da Figura 3</h6>
</div>
  
<h4>5.2.2) Módulos criados pelo programador</h4>
Para importamos dentro do código um módulo que nós mesmos criamos, basta que os dois arquivos estejam dentro da mesma pasta. Vamos primeiramente criar um módulo simples que define uma função que calcula o dobro de um número inserido pelo usuário. Chamaremos esse módulo de vezesdois.py.

<div align="center">
  <img height="150em" src="../img/functions/fig9.png"/>
  <h6>Figura 9 – Módulo criado por nós, vezesdois.py</h6>
</div>

Agora escrevemos um programa que solicita ao usuário que insira um número. Importamos nosso módulo vezesdois, pedimos um número ao usuário e chamamos a função dobro de vezesdois, passando o valor do usuário como parâmetro da função.

<div align="center">
  <img height="150em" src="../img/functions/fig10.png"/>
  <h6>Figura 10 – Nosso programa, que utiliza a função dobro do módulo vezesdois</h6>
</div>
  
Salvamos nosso programa como boraver.py, na mesma pasta que nosso módulo.

<div align="center">
  <img height="150em" src="../img/functions/fig11.png"/>
  <h6>Figura 11 – Os arquivos devem estar na mesma pasta</h6>
</div>
  
Executamos agora nosso programa boraver.py normalmente no prompt de comando.

<div align="center">
  <img height="150em" src="../img/functions/fig12.png"/>
  <h6>Figura 12 – Executando o código que criamos, que chama o módulo que criamos. Dá muito trabalho ser um programador tão autossuficiente...</h6>
</div>
