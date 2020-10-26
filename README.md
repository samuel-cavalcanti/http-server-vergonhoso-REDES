# http server vergonhoso

## TAREFAS
 
1. Execute o servidor HTTP fornecido e entenda o seu funcionamento
    1. Abra um navegador e acesse o endereço do servidor: 
    http://127.0.0.1:8080 Repare que a página exibirá sempre a mensagem “Hello, World!”,
    independentemente do que for solicitado pelo cliente.
    
    2. Abra um terminal e acesse por meio de telnet acesse o endereço do servidor: 
    ```shell script
   telnet 127.0.0.1 8080
    GET / HTTP 1.1
    ```
   Após o GET, dê dois “Enter”. Será exibido o cabeçalho da mensagem (HTTP/1.1 200 OK)
   e também “Hello, World!”. Repare que independentemente do comando digitado,
   o servidor retornará sempre a mesma resposta.
   
1. Após realizar os testes acima, analise o código fonte da aplicação com o uso de
um editor de texto ou IDE de programação;

3. Faça as alterações necessárias no código para que o servidor seja capaz de processar
um pedido GET de um cliente e retornar um arquivo .html para o mesmo;

    1. Crie um arquivo index.html (na mesma pasta em que o servidor estiver sendo executado)
    com o código abaixo (como exemplo) para ser usado como resposta:
        ```html
       <html>
         <head><title>Este é o meu servidor!</title></head>
         <body>
              <h1>Olá mundo!</h1>
              O meu servidor funciona!
         </body>
        </html>
        ```
    2. Quando um pedido é feito ao servidor, a variável request (linha 35) recebe os
    dados solicitados. Esta variável deve ser inspecionada para que se possa analisar o
    que está sendo pedido. É a partir dela que devem ser tratados os casos abaixo solicitados.
    DICA: Esta variável request pode ser segmentada em pedaços de informação menores e
    consultados por índice (vetor).
    
    3. A sintaxe do pedido GET deve seguir a especificada pelo protocolo HTTP:
        ```shell script
           GET /caminho HTTP/versão
        ```
        Por exemplo:
        ```shell script
           GET /arquivo.html HTTP/1.1
        ```
       Caso o arquivo esteja em uma pasta:
        ```shell script
           GET /pasta/arquivo.html HTTP/1.1
        ```
       Outro exemplo:
       ```shell script
           GET / HTTP/1.1
        ```
       Neste caso quando não é especificado o arquivo no pedido, o servidor deve procurar
       pelo index.html.
       
       __IMPORTANTE__: Ao fazer um pedido com GET, nunca se deve inserir o caminho do arquivo no
       sistema de arquivos do sistema operacional, pois o HTTP não sabe interpretar esse caminho
       (exemplo a __NÃO__ usar: _C:\Documentos\pasta\arquivo.html_ ou _/home/usuario/arquivo.html_).
       Deve-se inserir apenas o caminho do arquivo em relação à pasta em que o servidor HTTP
       está rodando (caminho relativo).
       
      4. Caso o caminho solicitado não exista, o servidor deve retornar o código 404 -
      página não encontrada. Este retorno deve seguir a especificação do protocolo HTTP,
      onde são enviados dois comandos: um para ser interpretado apenas pelo navegador
      (primeira linha) e outro para ser lido pelo cliente (segunda linha em diante),
      como o exemplo abaixo. A primeira linha JAMAIS pode ser salva em um arquivo
      .html. Deve ser retornada pelo servidor antes do conteúdo/corpo da página.
          ```html
            HTTP/1.1 404 Not Found\r\n\r\n
            <html>
                   <head></head>
                <body>
                     <h1>404 Not Found</h1>
                </body>
            </html>
            \r\n
         ```
      5. Caso algum outro comando diferente de _GET_ seja digitado, o servidor deve tratar a
      exceção e retornar “comando desconhecido” e continuar aguardando por novos comandos.
      Neste caso, o erro deve ser:
          ```html
             HTTP/1.1 400 Bad Request\r\n\r\n
            <html>
               <head></head>
               <body>
                   <h1>400 Bad Resquest</h1>
               </body>
            </html>
            \r\n
          ```
      6. Recorde-se que caso a página seja realmente encontrada, o servidor deve retornar
      (na primeira linha) o comando _HTTP/1.1 200 OK \r\n\r\n_ . E só em seguida retornar o
      conteúdo da página html. A primeira linha __JAMAIS__ pode ser salva em um arquivo .html.
      Deve ser retornada pelo servidor antes do conteúdo/corpo da página;
      
      7. Sempre que um cliente enviar um comando GET para o servidor, este deve imprimir
      na tela (do terminal) todo o comando enviado pelo cliente. Ou seja, a variável
      request deve ser apresentada na tela do terminal que estiver executando o servidor;
      
      8. É importante lembrar que, por omissão, quando se faz um pedido diretamente à raiz
      (isto é: _GET /HTTP/1.1_), sem especificar uma página, o servidor deve retornar a página
      padrão (geralmente o _index.html_).
      
      __Atenção__: O servidor nunca deverá ser encerrado. Apenas os clientes terão as conexões abertas por
      mais tempo ou encerradas logo após um pedido.
    
4. Faça os testes do funcionamento do servidor usando o telnet, bem como o navegador.
É importante notar que o navegador faz mais de um pedido por vez, pois solicita um arquivo
favicon.ico (arquivo de ícone para a aba). É necessário tratar esta situação na implementação
do servidor (cabendo a vocês encontrar a melhor forma para este tratamento).

5. O objetivo ao final da implementação é que o servidor receba e responda às
solicitações dos clientes, independentemente do arquivo solicitado e do software
(navegador) que esteja sendo utilizado para o pedido. O servidor deve funcionar tanto
para o telnet quanto para o navegador.