# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['MiniFaceonPC.py'],
             pathex=['D:\\PycharmProjects\\fifa_faceon'],
             binaries=[],
             datas=[('.\\images\\Gradient\\*.png', 'images\\Gradient'), ('.\\images\\position\\*.png', 'images\\position'), ('.\\images\\icon.png', 'images'), ('.\\font\\*.ttf', 'font'), ('.\\font\\*.otf', 'font')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='MiniFaceonPC',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='icon.ico')
