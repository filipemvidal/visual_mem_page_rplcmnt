# Representação visual de algoritmos de substituição de página de memória

Projeto em Python para simular algoritmos de substituição de páginas e visualizar o comportamento da memória com duas saídas diferentes:

- console, para acompanhar passo a passo os acessos, page faults e remoções;
- PyGame, para exibir uma visualização gráfica das tabelas de memória e navegar entre os eventos da simulação.

O projeto trabalha com uma sequência fixa de referências de página e compara três algoritmos:

- FCFS/FIFO
- LRU
- LFU

## Ambiente de desenvolvimento

O ambiente utilizado para desenvolvimento foi:

- Linux via WSL 2
- Windows 11 como sistema hospedeiro
- Python com ambiente virtual dedicado

## Dependências

A única dependência do projeto é a biblioteca gráfica `pygame`.

## Como preparar o ambiente

Recomenda-se criar um ambiente virtual antes de instalar as dependências.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r py_requirements.txt
```

Se o sistema usar `python` no lugar de `python3`, o comando pode ser ajustado conforme a instalação local.

## Como executar

### Execução em console (CLI)

O ponto de entrada em console é [main.py](main.py). Ele executa a simulação para os três algoritmos e imprime o resultado no terminal.

```bash
python main.py
```

### Execução gráfica (GUI)

O ponto de entrada da interafce visual também é [main.py](main.py), porém é necessário adicionar a flag `gui`. Ela abre uma janela do PyGame com três tabelas, uma para cada algoritmo, e permite navegar pelos eventos com as teclas de seta esquerda e direita.

```bash
python main.py gui
```

## Visão geral da arquitetura

O código está organizado em camadas simples:

- `algorithms/`: implementação dos algoritmos de substituição de páginas.
- `controllers/`: camada de simulação e definição dos eventos usados entre as partes do sistema.
- `views/`: execução em console e interface gráfica.
- `pygame_classes/`: estrutura básica para renderização no PyGame.
- `main.py`: ponto de entrada.

## Documentação das classes

### `algorithms.base.PageReplacementAlgorithm`

Classe abstrata base para os algoritmos de substituição de páginas.

- `access(page)`: método obrigatório que processa o acesso a uma página e retorna um `SimulationEvent`.
- `get_frames()`: método obrigatório que retorna uma cópia dos frames atuais.

### `algorithms.fcfs.FCFS`

Implementa a estratégia First Come, First Served, também tratada no projeto como FIFO.

Atributos principais:

- `capacity`: capacidade máxima da memória.
- `frames`: lista com as páginas atualmente carregadas.
- `queue`: fila usada para decidir qual página será removida.

Métodos:

- `access(page)`: trata hits e page faults; ao estourar a capacidade, remove a página mais antiga da fila.
- `get_frames()`: retorna uma cópia dos frames.

### `algorithms.lru.LRU`

Implementa o algoritmo Least Recently Used.

Atributos principais:

- `capacity`: capacidade máxima da memória.
- `frames`: lista com as páginas carregadas.
- `recency`: lista que mantém a ordem de uso recente das páginas.

Métodos:

- `access(page)`: atualiza a ordem de recência nos hits e remove a página menos recente quando a memória enche.
- `get_frames()`: retorna uma cópia dos frames.

### `algorithms.lfu.LFU`

Implementa o algoritmo Least Frequently Used.

Atributos principais:

- `capacity`: capacidade máxima da memória.
- `frames`: lista com as páginas carregadas.
- `frequency`: dicionário com a frequência de acesso de cada página.
- `arrival_order`: lista para desempate entre páginas com a mesma frequência.

Métodos:

- `access(page)`: incrementa a frequência nos hits e remove a página menos frequente, usando a ordem de chegada como desempate.
- `get_frames()`: retorna uma cópia dos frames.

### `controllers.simulator.Simulator`

Camada simples que executa um algoritmo sobre uma sequência de referências.

Atributos principais:

- `algorithm`: instância concreta do algoritmo escolhido.

Métodos:

- `step(page)`: executa um único acesso na política configurada.
- `run(references)`: percorre a lista de páginas e retorna a lista de eventos gerados.

### `controllers.events.SimulationEvent`

Representa o resultado de um acesso a página.

Atributos:

- `algorithm`: nome do algoritmo.
- `page`: página acessada.
- `page_fault`: indica se houve page fault.
- `removed_page`: página removida, quando houver.
- `frames`: estado dos frames após o acesso.
- `metadata`: dados extras do algoritmo, como recência ou frequência.

### `controllers.events.ViewSimCell`

Estrutura auxiliar para a visualização gráfica.

Atributos:

- `page`: página exibida na célula.
- `detail`: marcação visual da célula, por exemplo `selected` ou `removed`.

### `controllers.events.ViewSimulationEvent`

Evento mais granular usado pela interface PyGame.

Atributos:

- `page`: página em destaque na cena.
- `frames`: lista de células de visualização.
- `page_fault`: indica se o estado deve destacar um page fault.

### `views.console.ConsoleView`

Responsável pela saída textual no terminal.

Atributos principais:

- `rows`: histórico estruturado dos passos da simulação.
- `events`: lista dos eventos recebidos.

Métodos:

- `__run_simulation(algorithm_class, capacity, references)`: roda a simulação de um único algoritmo.
- `run(references)`: roda a simulação dos três algoritmos.
- `__record(step, event)`: armazena o evento com o número do passo.
- `__render()`: exibe uma tabela resumida com os acessos.
- `__summary()`: imprime o total de acessos, page faults, hits e a taxa de acerto.

### `views.gui.GuiView`

Responsável por gerenciar a interafce gráfica.

Métodos:

- `__run_simulation(algorithm_class, capacity, references)`: roda a simulação de um único algoritmo.
- `run(references)`: inicializa o pygame e roda a simulação dos três algoritmos.

### `pygame_classes.basics.Object`

Classe base para os objetos renderizados na cena do PyGame.

Atributos principais:

- `x`, `y`: posição do objeto.
- `scene`: cena à qual o objeto pertence.

Métodos:

- `set_scene(scene)`: associa o objeto a uma cena.
- `update(surface, delta_time)`: contrato de atualização por frame.
- `set_position(x, y)`: altera a posição do objeto.

### `pygame_classes.basics.Sprite`

Versão de `Object` voltada para renderização de imagem.

Métodos principais:

- `update(surface, delta_time)`: desenha a sprite na tela.
- `draw(surface)`: renderiza a imagem carregada.

Observação: a classe existe no código, mas não é usada na versão final da interface.

### `pygame_classes.basics.Text`

Objeto de texto renderizável.

Atributos principais:

- `text`: conteúdo exibido.
- `font_size`: tamanho da fonte.
- `color`: cor do texto.
- `visible`: controla se o texto aparece na cena.

Métodos:

- `update(surface, delta_time)`: desenha o texto.
- `draw(surface)`: renderiza o texto na tela.
- `set_visible(visible)`: mostra ou oculta o texto.
- `set_text(text)`: altera o conteúdo.

Observação: assim como `Sprite`, foi criada para facilitar o desenvolvimento da interface.

### `pygame_classes.basics.Scene`

Gerencia um conjunto de objetos renderizados ao mesmo tempo.

Atributos principais:

- `surface`: superfície principal do PyGame.
- `objects`: lista de objetos da cena.

Métodos:

- `add_object(obj)`: adiciona um objeto à cena.
- `remove_object(obj)`: remove um objeto da cena.
- `update(delta_time)`: chama `update` de todos os objetos da cena.

### `pygame_classes.table.Table`

Representa a tabela visual da memória RAM na interface PyGame.

Atributos principais:

- `title`: título exibido acima da tabela.
- `cells`: lista de células atualmente visíveis.
- `max_cells`: limite de células da tabela.
- `page_fault_text`: texto exibido quando ocorre page fault.
- `procurando_text`: texto exibido enquanto a página está sendo buscada.
- `events_tracked`: lista de eventos intermediários usados para navegar na animação.

Métodos:

- `set_scene(scene)`: associa a tabela à cena e adiciona os textos auxiliares.
- `create_cell(text)`: cria uma nova célula visual.
- `add_cell(cell)`: adiciona uma célula já criada à tabela.
- `clear_cells()`: remove as células atuais da cena.
- `draw(surface)`: desenha a moldura e o título da tabela.
- `handle_simulation_events(events)`: converte eventos de simulação em eventos visuais mais detalhados.
- `handle_view_event(event)`: aplica um evento visual à tabela.
- `add_to_page_events(index)`: navega entre os eventos já processados.

### `pygame_classes.table.Cell`

Representa uma célula individual da tabela visual.

Atributos principais:

- `text`: texto exibido na célula.
- `table`: tabela à qual a célula pertence.
- `width`, `height`: dimensões da célula.
- `border_color`, `border_width`: estilo visual da borda.

Métodos:

- `set_selected(value)`: altera a aparência da célula conforme o estado visual.
- `set_table(table)`: redefine a tabela associada.
- `get_position()`: retorna a posição absoluta da célula.
- `set_position(_x, _y)`: altera a posição relativa da célula.
- `update(surface, delta_time)`: desenha a célula.
- `draw(surface)`: renderiza a borda e o texto.

## Fluxo de execução

Tanto o console quanto a interface gráfica seguem a mesma ideia:

1. é criada uma instância do algoritmo escolhido;
2. o `Simulator` percorre a sequência de referências;
3. cada acesso gera um `SimulationEvent`;
4. a camada de visualização consome esses eventos para exibir o resultado.

## Sequência de referência usada no projeto

Os exemplos atuais usam a sequência:

```python
[1, 2, 3, 1, 4, 2, 5, 1]
```

A capacidade da memória usada nos exemplos é de 3 páginas de memória.
