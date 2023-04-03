import pygame

pygame.init()

# ゲーム画面のサイズを設定する
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))

# フレームレートを設定する
clock = pygame.time.Clock()
FPS = 60
# ジョイスティックを初期化する
joystick_count = pygame.joystick.get_count()
joystick = pygame.joystick.Joystick(0)
joystick.init()

# コントローラーの軸の数を取得する
axis_count = joystick.get_numaxes()

# コントローラーのボタンの数を取得する
button_count = joystick.get_numbuttons()
def get_controller_input():
    # メインイベントループ内でこの関数を呼び出す

    # コントローラーの入力を処理する
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
            # 軸の値を取得する
            if event.axis == 0:
                # 左スティックの水平軸
                x_axis = event.value
            elif event.axis == 1:
                # 左スティックの垂直軸
                y_axis = event.value
            elif event.axis == 2:
                # 右スティックの水平軸
                z_axis = event.value

        elif event.type == pygame.JOYBUTTONDOWN:
            # ボタンが押されたとき
            if event.button == 0:
                # Aボタン
                a_button = True
            elif event.button == 1:
                # Bボタン
                b_button = True
            elif event.button == 2:
                # Xボタン
                x_button = True
            elif event.button == 3:
                # Yボタン
                y_button = True

        elif event.type == pygame.JOYBUTTONUP:
            # ボタンが離されたとき
            if event.button == 0:
                # Aボタン
                a_button = False
            elif event.button == 1:
                # Bボタン
                b_button = False
            elif event.button == 2:
                # Xボタン
                x_button = False
            elif event.button == 3:
                # Yボタン
                y_button = False

    return x_axis, y_axis, z_axis, a_button, b_button, x_button, y_button