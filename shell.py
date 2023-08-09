u = User.objects.create_user(username='my_User')
user = User.objects.create_user(username='Myaut')
Author.objects.create(user=user)

a1 = Author.objects.create(user=u)
Category.objects.create(name_of_category='Sport')
Category.objects.create(name_of_category='Chess'
Category.objects.create(name_of_category='Boats')
Category.objects.create(name_of_category='Ships')

Post.create.objects(
    author = 'Иванов Иван Иванович'
    positions = 'NW'
    header = 'All about Ships'
    text = 'Sjdljfhldkjfhsdfjhsdofjjs;dfkjs;dfskdjf;sldkjsdl;kfjhsdlfjsdfl;skjh'

)

Post.create.objects(
    author = 'Степан Иванович Кузнецов'
    positions = 'AT'
    header = 'All about Chess'
    text = 'Sjdljfhldkjfhsdfjhsdofjjs;dfkjs;dfskdjf;sldkjsdl;kfjhsdlfjsdfl;skjh'

)

Post.create.objects(
    author = 'Степан Иванович Кузнецов'
    positions = 'AT'
    header = 'All about me'
    text = 'Sjdljfhldkjfhsdfjhsdofjjs;dfkjs;dfskdjf;sldkjsdl;kfjhsdlfjsdfl;skjh'

)

# присвоить пост к категории
Category.objects.create(name_of_category='Ships')
Category.objects.create(name_of_category='Autobiography')
Category.objects.create(name_of_category='Authorsay')
PostCategory.objects.create(post=header('All about me'),category='Autobiography')
PostCategory.objects.create(post=header('All about me'),category='Authorsay')
PostCategory.objects.create(post=header('All about Ships'),category='Ships')

Comment.objects.create(post='All about me',user = user,text = 'skjddjv')
Comment.objects.create(post='All about Ships',user = user,text = 'skj2332v')
Comment.objects.create(post='All about Chess',user = u,text = 'skvvvvv')
Comment.objects.create(post='All about me',user = u,text = 's5632jv')

post = Post.objects.get(header='All about me')
post.like()#должен добавлять рейтинг к посту
anotherpost = Post.objects.get(header='All about Chess')
anotherpost.dislike()

u1 = User.objects.create_user(username='X')
u1.update_rating()#обновляем рейтинг пользователя

author = Author.objects.order_by('rating').last()#лучший пользователь
user = author.user
Author.objects.get(user=user).rating

post = Post.objects.order_by('rating').last
bestpost = post.post
Post.objects.values('time','author','rating','header').get(header=bestpost)


Comment.objects.values('time','user','rating','text').get(post=post)#все комментарии к этой статье



