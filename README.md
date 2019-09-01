<img align="right" hspace="20" src="https://img.shields.io/badge/ICX-v1.0.0-orange.svg?style=flat-square">

# iCX - Caixa Comportamental
Repositório dedicado ao projeto **iCX** (tarefa "CAIXA COMPORTAMENTAL DO RAMON") da disciplina "Fundamentos de Programação e Engenharia de Software - 2019.2" do IIN-ELS.

O **iCX** é uma aplicação python a ser executada em um modelo Raspberry (computador de placa única do tamanho reduzido) para automação de uma caixa comportamental posível de ser configurada remotamente.

<img src="https://img.shields.io/static/v1.svg?style=flat-square&label=PYTHON&message=3.7.4&color=blue"/> <img src="https://img.shields.io/static/v1.svg?style=flat-square&label=VSCODE&message=1.37.1&color=green"/> <img src="https://img.shields.io/static/v1.svg?style=flat-square&label=Git&message=2.21.0&color=inactive"/>

<br>

## Primeiros Passos: 
A seguir, será fornecido algumas informações e orientações básicas a respeito do iCX. Para maiores informações e os recursos por ele fornecidos, visite a [Wiki] do projeto.

#### Descrição das branches do projeto

- `master`: *branch principal que reflete a versão estável atual do software (integra todas as demais).*
- `graphic-user-interface`: *dedicada ao módulo de interface gráfica do software.*
- `monitoring`: *dedicada ao módulo que implementa os métodos de monitoramento em vídeo da caixa.*
- `training`: *dedicada ao módulo que implementa os métodos da rotina "training".*
- `reactivation`: *dedicada ao módulo que implementa os métodos da rotina "reactivation".*



## 1. Recursos necessários

**IMPORTANTE:** Para contribuir com o **iCX**, algumas ações devem ser realizadas para que tudo funcione corretamente. Primeiro certifique-se que você possuí instalados: 

- [Python 3.7] 
- [Git] 
- [VSCode] 
- [Git + VSCode] 
- [Github] 

## 2. Realizando "Fork" do repositório iCX:

   1. Logar na sua conta do Github;
   2. Acessar o [repositório icx]; 
   3. Clicar no botão "Fork" localizado no canto superior direito da página;
   4. Aguardar o processo ser concluído;
   5. Pronto você será redirecionado para a cópia do repositório em seu GtiHub;

## 3. Clonando o projeto:
 
**Utilizando VSCode**: 
O VSCode é totalmente integrado com o Git e torna a ação extremamente simples, se você tá começando a tralhar com controle de versão agora, essa é uma boa opção:

  1. Abra o Visual Studio Code.
  2. Tecle `Ctrl+Shift+P`, digite **"clone"** e tecle enter;
  3. Será solicitado a url do repositório iCX; 
  4. Digite: `https://github.com/iinels-pes-001/icx.git` e tecle enter;
  5. Escolha uma pasta onde você deseja que o projeto seja baixado;
  6. Aguarde o processo ser concluído;
  7. Pronto, basta clicar em **"Open Repository"**;

**Utilizando Terminal**: 
Caso deseje realizar a ação utilizando um terminal:

  1. Abra o Terminal;
  2. Navegue para o diretório que deseja baixar o projeto (Ex. `cd documents/git`);
  3. Execute o comando `git clone https://github.com/iinels-pes-001/icx.git`; 
  4. Tecle enter, digite usuário e senha github caso solicitado; 
  5. Aguarde o processo ser concluído;
  6. Tudo Pronto, seu clone local foi criado;
  7. Basta abrir o diretório imc criado com sua IDE favorita;

## 4. Executando o projeto

Para executar o módulo via terminal: 
1. Acesse o diretório do arquivo que deseja executar (Ex: ... `cd git/icx`); 
2. Execute o comando: `python3 main.py`

## 5. Sincronizando o "Fork" com repositório oficial:

Para manter seu "Fork" sincronizado com o repositório oficial, você deve:
1. [Configurar um *remote* para o *fork*];
2. [Sincronizar o fork];
3. [Relizar push (Remotes e forks)];

## Links Úteis
- :dart: [Quadro kanban do projeto] 
- :fire: [Issues do projeto] 
- :rocket: [Scrum em 9 minutos]
- :computer: [Git - guia prático] 
- :beetle: [VSCode] 
- :video_game: [Git + VSCode] 
- :snake: [Python]

## Wiki

Para maiores informações sobre o **iCX** e os recursos por ele fornecidos, visite a [Wiki] do projeto.

## Equipe

**@alexaquino**
* `Email: alexaquino.it@gmail.com`
* `Codepen: codepen.io/alexaquino`
* `Instagram: instagram.com/alexaquino_it`


**@brunospinelli**
* `Email: brunoguedesspinelli@hotmail.com`


**@pablogneuro**
* `Email: pabloqueiroz5@gmail.com`


**@Rhamaral**
* `Email: rodrigohoa@gmail.com`

**@larissaplopes**
* `Email: larissaplopes@outlook.com`

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.


<!-- Links -->

[Python 3.7]: https://www.python.org/downloads/
[Git]: https://git-scm.com/
[Github]: https://github.com
[repositório iCX]: https://github.com/iinels-pes-001/icx
[url icx]: https://github.com/iinels-pes-001/iCX
[Wiki]: https://github.com/iinels-pes-001/iCX/wiki
[Configurar um *remote* para o *fork*]: https://help.github.com/en/articles/configuring-a-remote-for-a-fork
[Sincronizar o fork]: https://help.github.com/en/articles/syncing-a-fork
[Relizar push (Remotes e forks)]: https://help.github.com/en/articles/pushing-commits-to-a-remote-repository
[Quadro kanban do projeto]: https://github.com/iinels-pes-001/iCX/projects/1
[Issues do projeto]: https://github.com/iinels-pes-001/iCX/issues
[Scrum em 9 minutos]: https://www.youtube.com/watch?time_continue=3&v=XfvQWnRgxG0
[Git - guia prático]: https://rogerdudler.github.io/git-guide/index.pt_BR.html
[VSCode]: https://code.visualstudio.com/
[Git + VSCode]: https://code.visualstudio.com/docs/editor/versioncontrol
[Python]: https://www.python.org/


