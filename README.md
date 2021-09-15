# NanoPiNEO2Testes

Guia prático inicialização.

<img src="https://wiki.friendlyarm.com/wiki/images/3/3c/NanoHat_Oled1.png" alt="nanopi oled" width="500" height="600"><img src="https://wiki.friendlyarm.com/wiki/images/3/32/NanoHat_OLED_nanopi_NEO.jpg" alt="nanopioled" width="500" height="600">

### downloads 

https://www.armbian.com/nanopi-neo-2/

https://redirect.armbian.com/nanopineo2/Focal_current

## Preparation

Certifique-se de ter um cartão SD bom e confiável e uma fonte de alimentação adequada. Imagens RAW podem ser gravadas com Etcher (todos os sistemas operacionais). Onde as imagens são compactadas com .xz, você pode gravá-las no cartão SD com o Etcher diretamente. 

## Boot

Resultados de tradução
Insira o cartão SD no slot, conecte um cabo à sua rede se possível ou um monitor e alimente a placa. (Primeira) inicialização (com DHCP) leva até 35 segundos com um cartão SD classe 10. 

## Login

Faça login como: root Password: 1234. Em seguida, você será solicitado a alterar essa senha (configuração do teclado americano). Quando terminar, você será solicitado a criar uma conta de usuário normal para suas tarefas diárias::
```
  $ sudo usermod -a -G i2c,spi,gpio pi
  $ sudo apt install python3-dev python3-pip libfreetype6-dev libjpeg-dev build-essential
  $ sudo apt install libsdl-dev libportmidi-dev libsdl-ttf2.0-dev libsdl-mixer1.2-dev libsdl-image1.2-dev
```


  
 
