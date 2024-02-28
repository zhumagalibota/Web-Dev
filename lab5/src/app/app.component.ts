import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  products = [
    { 
      image: 'assets/images/1.jpg',
      name: 'Книга Толкин Дж. Р. Р.: Властелин колец (пер. Каррик, Каменкович)',
      description: 'В 1937 году был написан "Хоббит", а в середине 1950-х годов увидели свет три книги "Властелина колец", повествующие о Средиземье - мире, населенном представителями волшебных рас со сложной культурой, историей и мифологией.',
      rating: 5,
      link: 'https://kaspi.kz/shop/p/tolkin-dzh-r-r-vlastelin-kolets-per-karrik-kamenkovich--26004983/?c=750000000'
    },
    { 
      image: 'C:\Users\zhuma\project\Web-Dev-2\lab5\src\assets\images\\2.jpg',
      name: 'Книга Толкин Дж. Р. Р.: Хоббит (с илл. Алана Ли)',
      description: 'В 1937 году был написан "Хоббит", а в середине 1950-х годов увидели свет три книги "Властелина колец", повествующие о Средиземье - мире, населенном представителями волшебных рас со сложной культурой, историей и мифологией.',
      rating: 5,
      link: 'https://kaspi.kz/shop/p/tolkin-dzh-r-r-hobbit-s-ill-alana-li--26005142/?c=750000000'
    },
    { 
      image: 'C:\Users\zhuma\project\Web-Dev-2\lab5\src\assets\images\\3.jpg',
      name: 'Книга Толкин Дж. Р. Р: Сильмариллион (с илл. Т. Несмита)',
      description: '"Сильмариллион" - один из масштабнейших миров в истории фэнтези, мифологический канон, который Джон Руэл Толкин составлял на протяжении всей жизни. of Product 2',
      rating: 5,
      link: 'https://kaspi.kz/shop/p/tolkin-dzh-r-r-sil-marillion-s-ill-t-nesmita--101138247/?c=750000000'
    },
    { 
      image: 'C:\Users\zhuma\project\Web-Dev-2\lab5\src\assets\images\\4.jpg',
      name: 'Книга Толкин Дж. Р. Р.: Дети Хурина. Нарн и Хин Хурин',
      description: 'жанр: фантастика, переплет: твердый переплет',
      rating: 4.5,
      link: 'https://kaspi.kz/shop/p/tolkin-dzh-r-r-deti-hurina-narn-i-hin-hurin-100715599/?c=750000000'
    },
    { 
      image: 'C:\Users\zhuma\project\Web-Dev-2\lab5\src\assets\images\\5.jpg',
      name: 'Книга Толкин Дж. Р. Р.: Неоконченные предания Нуменора и Средиземья',
      description: 'В 1980 году его сын Кристофер подобрал и издал первый сборник, "Неоконченные предания Нуменора и Средиземья", в котором рассказывается о персонажах, событиях и географических объектах, вскользь упомянутых во "Властелине Колец": о потере Кольца Всевластья на Ирисных полях, о происхождении Гэндальфа, об основании Рохана и многом другом.',
      rating: 5,
      link: 'https://kaspi.kz/shop/p/tolkin-dzh-r-r-neokonchennye-predanija-numenora-i-sredizem-ja-26005059/?c=750000000'
    },
    { 
      image: 'C:\Users\zhuma\project\Web-Dev-2\lab5\src\assets\images\\6.jpg',
      name: 'Книга Толкин Дж. Р. Р.: Падение Гондолина',
      description: 'жанр: фантастика, переплет: твердый переплет',
      rating: 5,
      link: 'https://kaspi.kz/shop/p/tolkin-dzh-r-r-padenie-gondolina-102333779/?c=750000000'
    },
    { 
      image: 'C:\Users\zhuma\project\Web-Dev-2\lab5\src\assets\images\\7.jpg',
      name: 'Книга Льюис К. С.: Хроники Нарнии. Последняя битва',
      description: 'жанр: фантастика, переплет: твердый переплет',
      rating: 0,
      link: 'https://kaspi.kz/shop/p/l-juis-k-s-hroniki-narnii-poslednjaja-bitva-114213327/?c=750000000'
    },
    { 
      image: 'C:\Users\zhuma\project\Web-Dev-2\lab5\src\assets\images\\8.jpg',
      name: 'Книга Льюис К. С.: Хроники Нарнии. Начало истории',
      description: 'жанр: фантастика, переплет: твердый переплет',
      rating: 0,
      link: 'https://kaspi.kz/shop/p/l-juis-k-s-hroniki-narnii-nachalo-istorii-114214075/?c=750000000'
    },
    { 
      image: 'C:\Users\zhuma\project\Web-Dev-2\lab5\src\assets\images\\9.jpg',
      name: 'Книга Набор книг "Властелин колец". (Дж. Р. Р. Толкин) автор.',
      description: 'жанр: чтение на иностранных языках',
      rating: 0,
      link: 'https://kaspi.kz/shop/p/nabor-knig-vlastelin-kolets-dzh-r-r-tolkin-avtor--111973414/?c=750000000'
    },
    { 
      image: 'C:\Users\zhuma\project\Web-Dev-2\lab5\src\assets\images\\10.jpg',
      name: 'Книга Толкин Джон Роналд Руэл: Собрание набросков и рисунков к "Властелину Колец"',
      description: 'жанр: неадаптированная литература',
      rating: 0,
      link: 'https://kaspi.kz/shop/p/tolkin-dzhon-ronald-ruel-sobranie-nabroskov-i-risunkov-k-vlastelinu-kolets--111973678/?c=750000000'
    }
  ];

  
}
