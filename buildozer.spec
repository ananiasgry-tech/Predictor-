[app]
title = Predictor 
package.name = predictor 
package.domain = org.exemplo
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy

# (Abaixo, garanta que estas permissões estejam ativas se o app usar internet)
android.permissions = INTERNET
android.archs = armeabi-v7a, arm64-v8a
