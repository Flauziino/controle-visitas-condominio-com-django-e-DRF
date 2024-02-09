# Documentação do Projeto "Controle de Visitantes com Django"

## Introdução

O "Controle de Visitantes com Django" é uma aplicação desenvolvida utilizando Python com o framework Django, HTML e CSS. A finalidade do sistema é gerenciar o controle de acesso de visitantes em um condomínio fechado. Cada componente do projeto é organizado em apps individuais, focados em funcionalidades específicas.

## Estrutura do Projeto

### Apps do Projeto

**Usuarios:**

+ Responsável pela autenticação e controle de usuários do sistema.

**Quartos:**

+ Gerencia informações sobre os quartos disponíveis no condomínio.

**Porteiros:**

+ Lida com os dados dos membros da portaria responsáveis pelo atendimento.

**Visitantes:**

+ Gerencia informações sobre os visitantes, desde o registro até a autorização e finalização da visita.

## Funcionalidades Gerais

### Dashboard Principal (Index):

+ A página principal exibe uma dashboard com informações cruciais sobre o condomínio, incluindo visitantes aguardando autorização, em visita e visitas finalizadas. Também são apresentadas estatísticas gerais.

### Registrar Visitante:

+ A funcionalidade permite que a equipe da portaria registre um novo visitante, incluindo informações como nome, CPF, data de nascimento, número da casa a ser visitada, placa do veículo, entre outros.

### Autorização de Visita:

+ A autorização de visita é realizada pela equipe da portaria, indicando o morador responsável pela autorização.
### Finalização de Visita:

+ A finalização de uma visita altera o status do visitante para "FINALIZADO" e registra o horário de saída.

## Apps Individuais

### Usuarios:

+ Responsável por lidar com a autenticação e controle de usuários. Utiliza o modelo Usuario que estende o modelo padrão do Django, permitindo diferentes permissões.

### Dashboard:

+ Responsável pela exibição da dashboard no index da aplicação, exibe numeros como: todos os visitantes, os visitantes aguardando para serem aprovados, visitantes em visita, e as visitas finalizadas além de ter dados para todos os visitantes do mes.
### Porteiros:

+ Lida com os dados dos membros da portaria, incluindo informações como nome completo, CPF, telefone e data de nascimento.
### Visitantes:

+ Responsável por gerenciar informações sobre os visitantes. Utiliza o modelo Visitante que representa as informações detalhadas de um visitante, incluindo status, nome completo, CPF, data de nascimento, número da casa, placa do veículo, horários relevantes e outras informações.
## Considerações Finais

O sistema fornece uma interface eficiente para o controle de visitantes em condomínios, permitindo que a equipe da portaria realize operações essenciais com facilidade. Contribuições são bem-vindas para a melhoria contínua do projeto.

Autor: Flauziino - Desenvolvedor

Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir um pull request ou relatar problemas abrindo uma issue.