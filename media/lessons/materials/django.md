## Class Meta
***

* É uma classe criada na model para expor informações da modelo

* **verbose_name e verbose_name_plural**: São o nome da classe em modo para leitura humana e o nome da classe no plural

* **unique_together = (('user', 'course'),)**: Recebe uma tupla de tuplas, só pode existir um model cadastrado no sistema para cada usuário e curso, evitando assim repetições

* **ordering = ['name']**: Ordenar as tabelas pelo atributo name


## Fields
***

#### Choices

```py
STATUS_CHOICES = (
  (0, 'Pendente'),
  (1, 'Aprovado'),
  (2, 'Cancelado'),
)
status = models.IntegerField('Situação', choices=STATUS_CHOICES, default=0, blank=True)
```


## Filtros
***

#### date

* Formata a data para o formato dia/mes/ano_com_4_digitos
```html
<!-- 21/08/1993 -->
</p>{{course.start_date|date:'d/m/Y'}}</p>
```

#### timesince

* Gera o texto há 5 horas, há 2 dias e etc... através da data passada comparando com a hora atual
```html
<!-- Começou há 3 dias atrás -->
<p>Começou há {{course.start_date|timesince}} atrás</p>
```

#### default

* Insere um valor default caso esteja em branco o campo
```html
</p>{{course.start_date|date:'d/m/Y'|default:"Não informado"}}</p>
```

#### linebreaks e linebreaksbr

* Quebra um texto em paragrafos \<p\>\</p\>
```html
{{course.description|linebreaks}}
```

* O **linebreaksbr** serve para quando você já está dentro de um paragrafo

#### truncatewords

* Quebrar o texto na quantidade de palavras passados como argumento utilizando o ..., no caso são 20 palavras
```html
</p>{{course.description|truncatewords:'20'}}</p>
```

#### safe

* Diz para o django que o conteudo inserido é seguro, não há nada malicioso, usado só quando você confia na pessoa que está inserindo o conteudo, por exemplo, inserir um vídeo embedded, logo o usuário pode inserir algo malicioso
```html
{{material.embedded|safe}}
```

#### pluralize

* Dependendo da quantidade de objetos ele pluraliza o objeto em questão, por exemplo se tiver 1 curso ele não irá inserir o **s**, caso tiver mais de 1 curso ele insere, **pluralize:"singular, plural"**
```html
<p>Curs{{course.count|pluralize:"o,os"}}</p>
```


## Tags
***

#### with

* Serve para realizar determinadas ações jogue numa variável e essa variável possa ser usada em um determinado bloco para não haver repetições de código
```html
{% with qtd_course=couses.count %}
  <p>{{course}} tem {{qtd_course}} comentario{{qtd_course|pluralize}}
{% endwith %}
```

## Admin
***

#### list_filter

* Filtragem lateral por data, pode ser também por algum atributo que tenha a choice
```py
list_filter = ['created_at']
```

#### TabularInline e StackedInline

* Podemos inserir uma model dentro de outra no admin, normalmente usado quando há relacionamentos
```py
from .models import Material, Lesson

class MaterialAdmin(admin.StackedInline):
  model = Material
  
class LessonAdmin(admin.ModelAdmin):
  ...
  inlines = [MaterialAdmin]
  
admin.site.register(Lesson, LessonAdmin)
```


