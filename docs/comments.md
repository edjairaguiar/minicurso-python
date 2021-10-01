# COMENTÁRIOS EM PYTHON

Desde os primórdios da programação, o uso de comentários é essencial para a comunicação do grupo e também como lembrete pessoal. 
Os comentários em programação, como você já deve saber, têm diversos usos: documentá-lo, adicionar descrição, ou mesmo, marcar um bloco de linhas, explicar o funcionamento de uma função... 
A parte interessante dos comentário é que essas linhas não são lidas pelo compilador; muito pelo contrário: elas são completamente ignoradas, aparecendo somente quando o arquivo é aberto em um editor de texto.

Existem duas formas de escrever comentários em Python:
<ul>
<li>Um tipo de comentário para definirmos que uma única linha deve ser ignorada;
<li>Comentários de blocos; ou seja, um conjunto de linhas delimitando o início e o fim do comentário.
</ul>

Abaixo, descrevemos as notações utilizadas:

## 1) NOTAÇÃO INLINE

Utilizamos o caractere "#" (também conhecido como <i>cerquilha</i> ou <i>sustenido</i>; ou, ainda, <i>hashtag</i>) para demarcarmos que tudo que estiver a frente desse caractere é um comentário. Esse caractere, portanto, ignora tudo que estiver até o final da linha em que é chamado.
  
  ```python 
  #tudo que estiver até o final da linha após a chamada do # será ignorado
  print(teste) #a instrução atrás # interpretada` 
  ```

## 2) NOTAÇÃO MULTILINE

Essa notação demarca um conjunto de linhas deve ser ignorado pelo compilador. 
Essa notação se dá pelo uso de 3 aspas simples ou 3 aspas duplas. Isso permite fazer comentários em blocos, como mostrando no exemplo a seguir:
  
  ```python 
  '''
    toda informações contidas entre 3 aspas SIMPLES
    é considerada um comentário.
  '''

  """
    informações mencionadas dentro de 3 aspas DUPLAS
    também são consideradas comentários
  """

  qualquer coisa fora do bloco de comentários é considerado código e deve seguir a sintaxe da linguagem.
  ```

Há uma diferença bastante interessante sobre essas duas notações. <br /><br />
Primeiramente, podemos ressaltar que um comentário pode aparecer no inicio da linha ou após espaço em branco ou código, mas não dentro de uma string literal. O caracterer cerquilha dentro de uma string literal é apenas uma cerquilha. 
Em seguida, destacamos que a notação multiline também pode ser chamada de <i>docstrings</i>. <br /><br />
As docstrings são mais comumente introduzidas no início de uma classe, de uma função ou no início do programa para definir o escopo do software ou o escopo de métodos. Para quem está lendo o código do programa não existe muita diferença, além da estética, entre comentários inline e docstrings, já que ambos são vistos como comentários e não impactam o funcionamento do código.  Mas para o programador há uma diferença marcante: uma docstring, diferentemente de um comentário, não é ignorada pelo interpretador, mas passa a fazer parte do objeto sobre o qual ela foi definida, podendo ser acessada através do help.
