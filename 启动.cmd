::set http_proxy=127.0.0.1:3128
::set https_proxy=127.0.0.1:20171
start "�ջ������" cmd /c "for /l %%a in (0,0,1) do python �ջ������.py"
start "�˷�����" cmd /c "python �˷�����.py & pause"
start "����" cmd /c "for /l %%a in (0,0,1) do python ����.py"
start "��" cmd /c "python ��.py & pause"