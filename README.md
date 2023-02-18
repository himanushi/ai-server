# Local AI Chatbot
このリポジトリは、Hugging Face の Transformers ライブラリを使用して、ローカル環境で簡単に対話型AIモデルを実装し、インタラクティブな対話を行うことができます。対話モデルは Hugging Face の提供する多くの学習済みモデルを使用することができ、自分で学習したモデルを使うこともできます。

# 事前準備
[Hugging Face](https://huggingface.co/)でアカウントを作成し、以下コマンドでログインしておいてください

```
huggingface-cli login
```

以下コマンドでログイン確認

```
huggingface-cli whoami
```

# 必要なライブラリ
transformers
これらのライブラリは以下のようにしてインストールできます。

```
pip install -r requirements.txt
```

使い方
以下のようにコマンドを実行すると、指定したモデルとの対話を開始することができます。

```python
python chat.py モデル名 "対話を開始する最初のメッセージ"
```

例えば、gpt2モデルを使用して対話を開始するには、次のようにコマンドを実行します。

```python
python chat.py gpt2 "こんにちは"
```

# 使用可能なモデル
このリポジトリで使用できるHugging Faceの学習済みモデルの例を以下に示します。完全なリストについては、Hugging Face のモデルページを参照してください。

## GPT系
gpt
gpt2
gpt2-medium
gpt2-large
gpt2-xl
## T5系
t5-small
t5-base
t5-large
## BART系
bart-base
bart-large
bart-large-cnn
bart-large-mnli
bart-large-xsum
## 日本語対応モデル
rinna/japanese-gpt2-medium
japanese-gpt2

# ライセンス
このリポジトリのコードはMITライセンスの元で公開されています。Hugging Face で提供されるモデルには、それぞれ異なるライセンスが適用されますので、Hugging Faceのサイトでライセンスを確認してください。
