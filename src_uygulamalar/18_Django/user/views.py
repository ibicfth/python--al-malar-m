from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt ##bu olmayınca session id hata veriyor
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username =username , password = password)
        if user is not None:
            #session_id oluşturmamız lazım login() methodu session id oluşturur.
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, 'başarıyla giriş yapıldı...')
            print('login başarılı')
            return redirect('layout_index')

        else:
            messages.add_message(request, messages.ERROR, 'kullanıcı adı yada parola hatalı...')
            print('kullanıcı adı yada parola yanlış')
            return redirect('login')

    else:
        return render(request,'user/login.html')

def register(request):
    if request.method == 'POST':
       
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        repassword=request.POST['repassword']

        if password == repassword:
            
            if User.objects.filter(username=username):
                messages.add_message(request, messages.WARNING, 'bu username daha önce alınmış ...')
                print('bu username daha önce alınmış ...')
                return redirect('register')

            else:
                if User.objects.filter(email=email):
                    messages.add_message(request, messages.WARNING, 'bu email zaten kayıtlı...')
                    print('bu email zaten kayıtlı...')
                    return redirect('register')

                else:
                    user=User.objects.create_user(username = username, email = email, password = password)
                    user.save()
                    messages.add_message(request, messages.SUCCESS, 'başarıyla kayıt yapıldı...')
                    
                    print('kayıt başarıyla gerçekleştirildi ...')
                    return redirect('login')
        else:
            messages.add_message(request, messages.ERROR, 'parolalar eşleşmiyor ...')
            print('')
            return redirect('register')

    else:
        
        return render(request,'user/register.html')

def logout(request):
    if request.method == 'POST':
        ##çıkış için logout methodunu kullanırız.
        auth.logout(request)
        messages.add_message(request,messages.SUCCESS,'başarıyla çıkış yapıldı...')
        return redirect('login')



