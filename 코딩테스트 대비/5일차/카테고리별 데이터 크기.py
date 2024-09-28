'''
## 문제

컴퓨터에 여러가지 파일이 있다. 파일의 종류는 다음과 같다.

- music (확장자 : mp3, aac, flac)
- image (확장자 : jpg, bmp, gif)
- movie (확장자 : mp4, avi, mkv)
- other (위와 다른 확장자들, 예 : 7z, txt, zip)

문자열로 예시 입력처럼 당신의 컴퓨터에 있는 파일명과 용량이 입력된다고 했을때 각 종류별로 용량을 계산하여 출력하라. 출력의 순서는 music > image > movie > other 순서이다.

입력은 문자열 배열 `strings`이고, 각 문자열에는 파일명과 용량이 기록되어 있다.

용량의 단위는 `'b'`이며, 파일명과 용량은 공백 `' '`으로 구분된다.

## 입력설명

- `0 < s.length <= 10000`

## 출력설명

종류별 용량을 순서대로 정수 배열로 출력

## 매개변수 형식

`strings = {"mv.song.mp3 11b", "greatSong.flac 1000b", "not3.txt 5b", "video.mp4 200b", "game.exe 100b", "mov1e.mkv 10000b"}`

## 반환값 형식

`{1011, 0, 10200, 105}`

[*** 풀이 (Python) (100/100) ***]
'''

def solution(strings):
    music = []
    image = []
    movie = []
    other = []
    for i in range(len(strings)):
        if 'mp3' in strings[i] or 'aac' in strings[i] or 'flac' in strings[i]:
            music.append(strings[i])
        elif 'jpg' in strings[i] or 'bmp' in strings[i] or 'gif' in strings[i]:
            image.append(strings[i])
        elif 'mp4' in strings[i] or 'avi' in strings[i] or 'mkv' in strings[i]:
            movie.append(strings[i])
        else:
            other.append(strings[i])

    music_data = []
    music_score = 0
    if len(music) != 0:
        for k in range(len(music)):
            for i in range(len(music[k])):
                for j in range(i, len(music[k])):
                    if music[k][i] == ' ' and music[k][j] == 'b':
                            music_data.append(music[k][i+1:j])
        for i in range(len(music_data)):
            music_score += int(music_data[i])
    else:
        music_score = 0

    image_data = []
    image_score = 0
    if len(image) != 0:
        for k in range(len(image)):
            for i in range(len(image[k])):
                for j in range(i, len(image[k])):
                    if image[k][i] == ' ' and image[k][j] == 'b':
                            image_data.append(image[k][i+1:j])
        for i in range(len(image_data)):
            image_score += int(image_data[i])
    else:
        image_score = 0

    movie_data = []
    movie_score = 0
    if len(movie) != 0:
        for k in range(len(movie)):
            for i in range(len(movie[k])):
                for j in range(i, len(movie[k])):
                    if movie[k][i] == ' ' and movie[k][j] == 'b':
                            movie_data.append(movie[k][i+1:j])
        for i in range(len(movie_data)):
            movie_score += int(movie_data[i])
    else:
        movie_score = 0
    
    other_data = []
    other_score = 0
    if len(other) != 0:
        for k in range(len(other)):
            for i in range(len(other[k])):
                for j in range(i, len(other[k])):
                    if other[k][i] == ' ' and other[k][j] == 'b':
                            other_data.append(other[k][i+1:j])
        for i in range(len(other_data)):
            other_score += int(other_data[i])
    else:
        other_score = 0
    answer = [music_score, image_score, movie_score, other_score]
    return answer

'''
모범답안

MUSIC_EXT = {'mp3', 'aac', 'flac'}
IMAGE_EXT = {'jpg', 'bmp', 'gif'}
MOVIE_EXT = {'mp4', 'avi', 'mkv'}
EXTs = [MUSIC_EXT, IMAGE_EXT, MOVIE_EXT]

def solution(strings):
    answer = [0, 0, 0, 0]
    for line in strings:
        name, size = line.split(' ')
        
        ext = name.split('.')[-1]
        size = int(size[:-1])

        for i, EXT in enumerate(EXTs):
            if ext in EXT:
                answer[i] += size
                break
        else:
            answer[3] += size
        

    return answer

'''