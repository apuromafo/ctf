# Hyperfiletable [Medium]

> **ES:** Sherlock DFIR sobre registro MFT: hash, usuario único, HTA malicioso (ZoneId, URL, tamaños), PowerPoint, credenciales en notas y conteo recursivo bajo `C:\Users\`.
> **EN:** DFIR sherlock over the MFT record: hash, sole user, malicious HTA (ZoneId, URL, sizes), PowerPoint, credentials in notes, and recursive count under `C:\Users\`.

| Campo | Valor |
|-------|-------|
| **Tipo** | DFIR |
| **URL** | https://app.hackthebox.com/sherlocks/hyperfiletable |
| **Evidencia** | hyperfiletable.zip |


:::info Sherlock Scenario

There has been a new joiner in Forela, they have downloaded their onboarding documentation, however someone has managed to phish the user with a malicious attachment. We have only managed to pull the MFT record for the new user, are you able to triage this information?

> [ZH] "在 Forela 中有一名新成员加入，他们已经下载了他们的入职文件，但是有人成功通过恶意附件钓鱼攻击了该用户。我们只能获取到该新用户的 MFT 记录，您能处理这些信息吗？"
> **ES:** Nuevo empleado con docs de onboarding que fue phisheado con adjunto malicioso: solo hay registro MFT, toca triarlo.
> **EN:** New joiner with onboarding docs was phished with a malicious attachment: only the MFT record is available, triage it.

:::

## 题目数据 / Datos / Data

[hyperfiletable.zip](./hyperfiletable.zip)

## Task 1 — Hash MD5 del MFT / MFT MD5 hash

> [ZH] "MFT 的 MD5 哈希值是多少？"
> **ES:** ¿Cuál es el hash MD5 del MFT?
> **EN:** What is the MD5 hash of the MFT?

```plaintext
File path and name: D:\Downloads\hyperfiletable\mft.raw\mft.raw
Name: mft.raw
Type: .raw
Size: 115.5 MB
Bytes: 121110528
Modified: 2023-06-02 22:38:10
Attributes: A
Copies: 1
CRC32: 29C15241
CRC64: 4EE3D6ED243B4347
MD5: 3730C2FEDCDC3ECD9B83CBEA08373226
```

```plaintext title="Answer"
3730C2FEDCDC3ECD9B83CBEA08373226
```

## Task 2 — Usuario único / Sole user

:::info

这里使用到 [MFTECmd](https://github.com/EricZimmerman/MFTECmd) 这款工具

> **ES:** Aquí se usa la herramienta [MFTECmd](https://github.com/EricZimmerman/MFTECmd).
> **EN:** This uses the [MFTECmd](https://github.com/EricZimmerman/MFTECmd) tool.

:::

> [ZH] "系统中唯一用户的名称是什么？"
> **ES:** ¿Cuál es el nombre del único usuario del sistema?
> **EN:** What is the name of the sole user on the system?

> **ES:** Parsear el MFT con `MFTECmd` y buscar la carpeta personal (`\user`) en el CSV resultante.
> **EN:** Parse the MFT with `MFTECmd` and search the resulting CSV for the personal folder (`\user`).

使用 `MFTECmd` 这款工具解析 mft 文件

```bash
PS D:\_Tool\_ForensicAnalyzer\MFTECmd> .\MFTECmd.exe -f D:\Downloads\hyperfiletable\mft.raw\mft.raw --csv "D:\Downloads\hyperfiletable\mft.raw"
MFTECmd version 1.2.2.1

Author: Eric Zimmerman (saericzimmerman@gmail.com)
https://github.com/EricZimmerman/MFTECmd

Command line: -f D:\Downloads\hyperfiletable\mft.raw\mft.raw --csv D:\Downloads\hyperfiletable\mft.raw

Warning: Administrator privileges not found!

File type: Mft

Processed D:\Downloads\hyperfiletable\mft.raw\mft.raw in 1.5877 seconds

D:\Downloads\hyperfiletable\mft.raw\mft.raw: FILE records found: 110,818 (Free records: 7,240) File size: 115.5MB
        CSV output will be saved to D:\Downloads\hyperfiletable\mft.raw\20240102085049_MFTECmd_$MFT_Output.csv
```

分析输出的结果文件，在其中搜索关键词 `\user`，即可得到用户个人文件夹的路径

```plaintext title="Answer"
Randy Savage
```

## Task 3 — HTA malicioso / Malicious HTA name

> [ZH] "被该用户下载的恶意 HTA 的名称是什么？"
> **ES:** ¿Cómo se llama el HTA malicioso descargado por ese usuario?
> **EN:** What is the name of the malicious HTA downloaded by that user?

> **ES:** Buscar por el directorio de descargas por defecto (`.\Users\Randy Savage\Downloads`); por volumen solo se muestra el registro relevante.
> **EN:** Search by the default downloads directory (`.\Users\Randy Savage\Downloads`); due to volume only the relevant record is shown.

使用用户的默认下载目录作为关键词进行搜索 `.\Users\Randy Savage\Downloads`

> 由于数据量较大，完整数据未在此体现

| EntryNumber | SequenceNumber | InUse | ParentEntryNumber | ParentSequenceNumber | ParentPath                     | FileName                       | Extension   | FileSize | ReferenceCount | ReparseTarget | IsDirectory | HasAds | IsAds | `SI<FN` | uSecZeros | Copied | SiFlags | NameType | Created0x10 | Created0x30 | LastModified0x10 | LastModified0x30 | LastRecordChange0x10 | LastRecordChange0x30 | LastAccess0x10 | LastAccess0x30 | UpdateSequenceNumber | LogfileSequenceNumber | SecurityId |
| :---------- | :------------- | :---- | :---------------- | :------------------- | :----------------------------- | :----------------------------- | :---------- | :------- | :------------- | :------------ | :---------- | :----- | :---- | :---- | :-------- | :----- | :------ | :------- | :---------- | :---------- | :--------------- | :--------------- | :------------------- | :------------------- | :------------- | :------------- | :------------------- | :-------------------- | :--------- |
| 103820      | 7              | TRUE  | 105011            | 2                    | .\Users\Randy Savage\Downloads | Onboarding.hta                 | .hta        | 1144     | 1              |               | FALSE       | TRUE   | FALSE | FALSE | FALSE     | FALSE  | Archive | Windows  | 21:40.1     |             | 21:45.6          | 21:40.1          | 21:45.6              | 21:40.2              | 22:01.0        | 21:40.1        | 27166224             | 375731114             | 1793       |
| 103820      | 7              | TRUE  | 105011            | 2                    | .\Users\Randy Savage\Downloads | Onboarding.hta:Zone.Identifier | .Identifier | 389      | 1              |               | FALSE       | FALSE  | TRUE  | FALSE | FALSE     | FALSE  | Archive | Windows  | 21:40.1     |             | 21:45.6          | 21:40.1          | 21:45.6              | 21:40.2              | 22:01.0        | 21:40.1        | 27166224             | 375731114             | 1793       |

即可找到答案

```plaintext title="Answer"
Onboarding.hta
```

## Task 4 — ZoneId del HTA / HTA ZoneId

> [ZH] "恶意 HTA 文件的 ZoneId 是多少？"
> **ES:** ¿Cuál es el ZoneId del HTA malicioso?
> **EN:** What is the ZoneId of the malicious HTA file?

> **ES:** El ADS `Zone.Identifier` del registro anterior contiene el `ZoneTransfer`.
> **EN:** The `Zone.Identifier` ADS from the previous record holds the `ZoneTransfer`.

上文记录的末尾就有

```plaintext
[ZoneTransfer]
ZoneId=3
HostUrl=https://doc-10-8k-docs.googleusercontent.com/docs/securesc/9p3kedtu9rd1pnhecjfevm1clqmh1kc1/9mob6oj9jdbq89eegoedo0c9f3fpmrnj/1680708975000/04991425918988780232/11676194732725945250Z/1hsQhtmZJW9xZGgniME93H3mXZIV4OKgX?e=download&uuid=56e1ab75-ea1e-41b7-bf92-9432cfa8b645&nonce=u98832u1r35me&user=11676194732725945250Z&hash=j5meb42cqr57pa0ef411ja1k70jkgphq
```

```plaintext title="Answer"
3
```

## Task 5 — URL de descarga del HTA / HTA download URL

> [ZH] "恶意 HTA 的下载 URL 是什么？"
> **ES:** ¿Cuál es la URL de descarga del HTA malicioso?
> **EN:** What is the download URL of the malicious HTA?

```plaintext title="Answer"
https://doc-10-8k-docs.googleusercontent.com/docs/securesc/9p3kedtu9rd1pnhecjfevm1clqmh1kc1/9mob6oj9jdbq89eegoedo0c9f3fpmrnj/1680708975000/04991425918988780232/11676194732725945250Z/1hsQhtmZJW9xZGgniME93H3mXZIV4OKgX?e=download&uuid=56e1ab75-ea1e-41b7-bf92-9432cfa8b645&nonce=u98832u1r35me&user=11676194732725945250Z&hash=j5meb42cqr57pa0ef411ja1k70jkgphq
```

## Task 6 — Tamaño asignado / Allocated size

:::info

接下来使用 [MFTExplorer](https://www.sans.org/tools/mftexplorer/) 这个工具

> **ES:** A continuación se usa la herramienta [MFTExplorer](https://www.sans.org/tools/mftexplorer/).
> **EN:** Next, this uses the [MFTExplorer](https://www.sans.org/tools/mftexplorer/) tool.

:::

> [ZH] "HTA 文件的分配大小是多少？（字节）"
> **ES:** ¿Cuál es el tamaño asignado (allocated) del HTA? (bytes)
> **EN:** What is the allocated size of the HTA file? (bytes)

> **ES:** En la salida de `MFTExplorer`, el atributo FileName indica `Physical Size: 0x1000`.
> **EN:** In the `MFTExplorer` output, the FileName attribute shows `Physical Size: 0x1000`.

在 `MFTExplorer` 的输出结果中，可以得到以下信息

```plaintext
**** FILE NAME ****
Type: FileName, Attribute #: 0x8, Size: 0x78, Content size: 0x5A, Name size: 0x0, Content offset: 0x18, Resident: True

File name: ONBOAR~1.HTA (Length: 0xC)
Flags: Archive, Name Type: Dos, Reparse Value: 0x0, Physical Size: 0x1000, Logical Size: 0x478
Parent Mft Record: Entry/seq: 0x19A33-0x2

Created On:  2023-04-05 13:21:40.0706726
Content Modified On: 2023-04-05 13:21:40.0732403
Record Modified On: 2023-04-05 13:21:40.2279587
Last Accessed On: 2023-04-05 13:21:40.0732403
```

```plaintext title="Answer"
4096
```

## Task 7 — Tamaño real / Real size

> [ZH] "HTA 文件的实际大小是多少？（字节）"
> **ES:** ¿Cuál es el tamaño real del HTA? (bytes)
> **EN:** What is the real size of the HTA file? (bytes)

```plaintext title="Answer"
1144
```

## Task 8 — Descarga del PowerPoint / PowerPoint download time

> [ZH] "用户何时下载了 PowerPoint 演示文稿？"
> **ES:** ¿Cuándo descargó el usuario la presentación PowerPoint?
> **EN:** When did the user download the PowerPoint presentation?

| EntryNumber | SequenceNumber | InUse | ParentEntryNumber | ParentSequenceNumber | ParentPath                          | FileName      | Extension | FileSize | ReferenceCount | ReparseTarget | IsDirectory | HasAds | IsAds | `SI<FN` | uSecZeros | Copied | SiFlags | NameType | Created0x10 | Created0x30 | LastModified0x10 | LastModified0x30 | LastRecordChange0x10 | LastRecordChange0x30 | LastAccess0x10 | LastAccess0x30 | UpdateSequenceNumber | LogfileSequenceNumber | SecurityId |
| :---------- | :------------- | :---- | :---------------- | :------------------- | :---------------------------------- | :------------ | :-------- | :------- | :------------- | :------------ | :---------- | :----- | :---- | :---- | :-------- | :----- | :------ | :------- | :---------- | :---------- | :--------------- | :--------------- | :------------------- | :------------------- | :------------- | :------------- | :------------------- | :-------------------- | :--------- |
| 105622      | 4              | FALSE | 107430            | 3                    | .\Users\Randy Savage\Documents\Work | Proposal.pptx | .pptx     | 16552989 | 1              |               | FALSE       | TRUE   | FALSE | FALSE | FALSE     | FALSE  | Archive | Windows  | 11:49.7     |             | 11:54.0          |                  | 12:14.6              | 11:54.0              | 11:54.0        |                | 26143496             | 375276644             | 1793       |

```plaintext
**** STANDARD INFO ****
Type: StandardInformation, Attribute #: 0x0, Size: 0x60, Content size: 0x48, Name size: 0x0, Content offset: 0x18, Resident: True

Flags: Archive, Max Version: 0x0, Flags 2: None, Class Id: 0x0, Owner Id: 0x0, Security Id: 0x701, Quota Charged: 0x0
Update Sequence #: 0x18EEB08

Created On:  2023-04-05 13:11:49.7425214
Content Modified On: 2023-04-05 13:11:53.9605745
Record Modified On: 2023-04-05 13:12:14.5858420
Last Accessed On: 2023-04-05 13:11:53.9605745
```

```plaintext title="Answer"
05/04/2023 13:11:49
```

## Task 9 — Contraseña en notas / Password in notes

> [ZH] "用户记录了他们的工作凭据，请问他们的密码是什么？"
> **ES:** El usuario anotó sus credenciales de trabajo: ¿cuál es la contraseña?
> **EN:** The user wrote down their work credentials: what is the password?

> **ES:** En los datos MFT de `.\Users\Randy Savage\Documents\Work\notes.txt` aparece el texto en claro.
> **EN:** The MFT data for `.\Users\Randy Savage\Documents\Work\notes.txt` shows the plaintext.

在 `.\Users\Randy Savage\Documents\Work\notes.txt` 的 MFT 数据中，得到以下明文信息

```plaintext
New onboarding process:
Download onboarding tool from Google Drive
Username: RSavage
Password: ReallyC00lDucks2023!
```

```plaintext title="Answer"
ReallyC00lDucks2023!
```

## Task 10 — Conteo bajo C:\Users\ / Count under C:\Users\

> [ZH] "在 `C:\Users\` 目录下还剩下多少个文件？（递归计算）"
> **ES:** ¿Cuántos ficheros quedan bajo `C:\Users\` (recursivo)?
> **EN:** How many files remain under `C:\Users\` (recursive)?

> **ES:** Filtrado en Excel por `ParentPath` (texto) y luego por `IsDirectory = FALSE`; el conteo puede variar según el CSV.
> **EN:** Excel filtering by `ParentPath` (text) then by `IsDirectory = FALSE`; the count may vary with the CSV.

这题可以直接借助 Excel 的强大的统计能力

首先，使用筛选功能，对 `ParentPath` 列的数据进行筛选，使用菜单中的文本筛选功能

然后将结果复制黏贴为新的工作表，将 `IsDirectory` 筛选为 `FALSE` 模式，继续筛选

:::warning  题目答案存在争议

我自己使用 `MFTECmd` 导出的 csv 报告进行筛选分析，但是出来的结果和标准答案不符合，不确定是哪里出现问题

> **ES:** Aviso: el conteo propio con el CSV de `MFTECmd` no coincidía con la respuesta oficial; posible discrepancia metodológica.
> **EN:** Caveat: my own count from the `MFTECmd` CSV did not match the official answer; possible methodology mismatch.

:::

```plaintext title="Answer"
3471
```

## Fuentes / Sources

- Dificultad y categoria: [momenbasel/htb-writeups - Sherlocks index](https://github.com/momenbasel/htb-writeups/blob/main/sherlocks/README.md) - fecha de acceso: 2026-09-24.
- Autor notas: Apuromafo.

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. Evidencia y respuestas con contexto, no solo la respuesta suelta.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Evidence and contextual answers, not bare answers.

_Fecha de edición: 2026-09-24_
