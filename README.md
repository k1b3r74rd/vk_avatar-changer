# repository_name
Program, written on python 3.7, for my certification.

Avatar auto-changer program. Place, where I use it ---> https://vk.com/avatarchanger

----------- HOW TO USE VK_AVATAR.PY -----------

  1. Firstly, you should do your own standalone app in VK, step-by-step: vk.com/dev -> My apps -> Create app -> Standalone app.
     Get app ID in Settings. Don't forget to turn it on.
  
  2. Get your USER access token with group and photo parameters (It's better to leave everything that is included).
     You can easily get it from https://vkhost.github.io/ by using your app ID.
     
     WARNING: Token is not infinite. If you want to get infinite token, read the information on this page: https://vk.com/dev/implicit_flow_user .
     
     
  3. Insert your access token, profile/group ID and desired time in the settings.ini. 
     You should remember, if you insert group ID, you should put minus in front of ID, like that: group_id = -ID
     If you put profile ID, you don't need to put minus.
  
  4. Put your avatars into 'pictures' directory.
  
  5. Start .py file.
  
  
  ----------- КАК ИСПОЛЬЗОВАТЬ VK_AVATAR.PY -----------
  
   1. Сперва вы должны сделать собственное standalone приложение в ВК, шаг за шагом: vk.com/dev -> Мои приложения -> Создать приложение -> Standalone-приложение.
      Получите ID приложения в Настройках. Не забудьте включить приложение.
   
   2. Получите ПОЛЬЗОВАТЕЛЬСКИЙ токен с параметрами группы и фото (Лучше оставить всё то, что включено).
      Токен можно просто получить с сайта https://vkhost.github.io/ , используя ID приложения.
      
      ВНИМАНИЕ: Токен не бесконечный. Если вы хотите получить бесконечный токен, прочитайте информацию на странице: https://vk.com/dev/implicit_flow_user .
      
      
   3. Вставьте ваш токен, ID профиля/группы и желаемое время в settings.ini.
      Вы должны знать, что если вы вставляете ID группы, то вы должны поставить минус перед самим ID, 
      чтобы получилось: group_id = -ID
      Если вы вставляете ID профиля, этого делать не надо.
      
   4. Скопируйте ваши аватары в папку 'pictures'
   
   5. Запустите .py файл.
