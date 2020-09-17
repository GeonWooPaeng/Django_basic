from django.shortcuts import render, redirect
from fcuser.models import Fcuser
from .models import Board
from .forms import BoardForm
# Create your views here.


def board_detail(request, pk):
    # 글 상세보기
    board = Board.objects.get(pk=pk) #입력받은 id의 글을 받아온다.
    return render(request, 'board_detail.html', {'board':board})

def board_write(request):
    if request.method == 'POST':
        # 로그인한 사용자가 자동으로 글쓰게 하기
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk=user_id)

            board = Board() 
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser
            board.save() 

            return redirect('/board/list/')

    else:
        form = BoardForm()

    return render(request, 'board_write.html', {'form': form})

def board_list(request):
    boards = Board.objects.all().order_by('-id') #모든것을 -정렬로 가지고 오겠다 => 최신것을 먼저 가지고 오겠다.
    return render(request, 'board_list.html', {'boards':boards})

