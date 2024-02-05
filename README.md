# Desafio-Tunt.Rocks-2024
Projeto do processo seletivo da Tunt.Rocks feito para realizar alterações em planilha.


# 🚀 Instalação
**Para utilizar o programa siga essas etapas:**

1. Verifique se você possui o Python instalado em sua máquina. Caso não o tenha, você pode instalá-lo clicando [nesse link](https://www.python.org/downloads/).

# 📋 Configuração da API do Google Sheets:
2. Você também precisará certificar-se de ter as dependências necessárias da API do Google Sheets para que o programa funcione. Utilize o terminal (CMD) com o seguinte comando:
```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

```

# 🐍 Usando o programa


**1. Para utilizar este programa, é necessario criar uma conta no [Google Cloud Plataform](https://cloud.google.com/?utm_source=google&utm_medium=cpc&utm_campaign=latam-BR-all-pt-dr-BKWS-all-all-trial-p-dr-1707800-LUAC0014411&utm_content=text-ad-none-any-DEV_c-CRE_512285710746-ADGP_Hybrid+%7C+BKWS+-+PHR+%7C+Txt+~+GCP_General-KWID_43700071226328534-kwd-472605895574&utm_term=KW_login+gcp-ST_Login+gcp&gad_source=1&gclid=EAIaIQobChMIvpPVjsaUhAMVj2JIAB0NoQuHEAAYASAAEgJLy_D_BwE&gclsrc=aw.ds&hl=pt_br)**

**2. Após a criação da conta, clique no botão "Selecionar um Projeto" no canto superior direito e em seguida em "Novo Projeto".**

**3. No console do Google Cloud, pesquise "Google Sheets API" e ative-a."**

**4. Depois de ativar a API, acesse "APIs e Serviços" -> "Credenciais"**

**5. No canto superior direito, clique no icone "Criar credenciais" e selecione a opção "ID do cliente OAuth"**

**6. Configure sua tela de concessões, utilizando um User Type externo, um nome qualquer e um e-mail de preferência pessoal.**

**7. Defina os escopos de sua preferência; após isso, salve e continuee**

**8. Volte às credenciais e crie um ID do Cliente OAuth, criando um "App para computador".**

**9. Após a criação, baixe o JSON do Cliente OAuth e renomei-o para "credentials.json"**

**10. Faça o download deste repositório e arraste o "credentials.json" para a mesma pasta do repositório após extraí-lo.**

**11. Abra o repositório na sua IDE e no seu próprio terminal, digite:**
```
python main.py
```
Caso prefira outra forma, você pode rodar o programa clicando no botão, localizado no canto superior direito da tela

![image](https://github.com/cauacodigos/Desafio-Tunt.Rocks-2024/assets/131932004/9058398f-66ab-4452-bb53-193478d30b45)

Se os passos forem seguidos corretamente, você verá a alteração da planilha nas colunas de situação e nota de aprovação final, respectivamente.

* **Planilha antes de executar o programa:**

![image](https://github.com/cauacodigos/Desafio-Tunt.Rocks-2024/assets/131932004/2c7058ba-d2f5-4255-a90b-036ac0973b8d)

* **Pós alteração:**

![image](https://github.com/cauacodigos/Desafio-Tunt.Rocks-2024/assets/131932004/0c148171-c967-4419-8b4c-73d8fa77c507)

# 📚 Referências

[^1]: Documentação do Google Sheets: https://developers.google.com/sheets/api/guides/concepts?hl=pt-br  [^1]


Planilha para testes: https://docs.google.com/spreadsheets/d/1nEag84LaTqSv_OjYCGRY7WfKVeiOTzIjnmmlE5f0WCI/edit#gid=0
