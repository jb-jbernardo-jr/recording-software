# Recording Software

## Instalação:

Para utilização desse programa, é necessário a instalação de algumas dependências, uma delas é criar um ambiente virtual Python.

Para isso execute o seguinte trecho de código em seu terminal para instalar o virtualenvwrapper:

```console
sudo apt install python3-pip
sudo pip install virtualenvwrapper
``` 

Feito isso, é necessário adicionar algumas variáveis de ambiente ao arquivo .bashrc (Localizado em $HOME/.bashrc). Utilizando seu editor de texto favorito adicione as seguintes variáveis:

```console
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_SCRIPT=/usr/local/bin/virtualenvwrapper.sh
source /usr/local/bin/virtualenvwrapper_lazy.sh
```

Após adicionado, salve o arquivo e atualize suas variáveis de ambiente:

```console
source .bashrc
```

Crie um ambiente virtual para instalar as dependências do projeto:

```console
mkvirtualenv _NOME_DO_AMBIENTE_
```

Para ativar o seu ambiente virtual use o seguinte comando:

```console
workon _NOME_DO_AMBIENTE_
```

E será dado o seguinte feedback caso tenha feito tudo corretamente:

```console
(_NOME_DO_AMBIENTE_) foo@bar:~$
```

Acesse o diretório de onde foi efetuado o download do repositório e instale as dependências presentes no arquivo "requirements.txt":

```console
pip install -r requirements.txt
```

Feito isso o projeto estará pronto para ser executado.

## Execução:

```console
python main.py
```