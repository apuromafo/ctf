# Noted [Easy]

> **ES:** Ficha mínima — ver plantilla completa en `../../_PLANIFICACION/PLANTILLA_SHERLOCK.md`.
> **EN:** Minimal header — see full template at `../../_PLANIFICACION/PLANTILLA_SHERLOCK.md`.

| Campo | Valor |
|-------|-------|
| **Tipo** | DFIR |
| **URL** | https://app.hackthebox.com/sherlocks/noted |
| **Evidencia** | Noted.zip |


:::info Sherlock Scenario

Simon, a developer working at Forela, notified the CERT team about a note that appeared on his desktop. The note claimed that his system had been compromised and that sensitive data from Simon's workstation had been collected. The perpetrators performed data extortion on his workstation and are now threatening to release the data on the dark web unless their demands are met. Simon's workstation contained multiple sensitive files, including planned software projects, internal development plans, and application codebases. The threat intelligence team believes that the threat actor made some mistakes, but they have not found any way to contact the threat actors. The company's stakeholders are insisting that this incident be resolved and all sensitive data be recovered. They demand that under no circumstances should the data be leaked. As our junior security analyst, you have been assigned a specific type of DFIR (Digital Forensics and Incident Response) investigation in this case. The CERT lead, after triaging the workstation, has provided you with only the Notepad++ artifacts, suspecting that the attacker created the extortion note and conducted other activities with hands-on keyboard access. Your duty is to determine how the attack occurred and find a way to contact the threat actors, as they accidentally locked out their own contact information. Warning : This sherlock requires an element of OSINT and players will need to interact with 3rd party services on internet.

> [ZH] "西蒙，Forela 的一名开发人员，向 CERT 团队报告了他的桌面上出现的一条笔记。……怀疑攻击者创建了勒索信并通过键盘访问进行了其他活动。……此 sherlock 需要 OSINT 的元素……"
> **ES:** Simon (dev de Forela) reporta nota de extorsión en el escritorio: robo de datos sensibles y amenaza de filtración en la dark web; solo se entregan artefactos Notepad++ (nota creada con acceso hands-on-keyboard); hay que reconstruir el ataque y recuperar el contacto bloqueado. Requiere OSINT.
> **EN:** Simon (Forela dev) reports an extortion note on his desktop: sensitive-data theft plus dark-web leak threat; only Notepad++ artifacts provided (note created via hands-on-keyboard); reconstruct the attack and recover the locked contact. OSINT required.

:::

## 题目数据 / Datos / Data

[Noted.zip](./Noted.zip)

## Task 1 — Script AWS de Simon / Simon's AWS script

> [ZH] "西蒙用于 AWS 操作的脚本的完整路径是什么？"
> **ES:** ¿Cuál es la ruta completa del script que Simon usaba para operaciones AWS?
> **EN:** What is the full path of the script Simon used for AWS operations?

> **ES:** Descomprimir la muestra (`\Noted\C\Users\Simon.stark\AppData\Roaming\Notepad++`) y revisar `config.xml` → historial de archivos recientes.
> **EN:** Extract the sample (`\Noted\C\Users\Simon.stark\AppData\Roaming\Notepad++`) and check `config.xml` → recent file history.

> **ES:** Estructura del zip: / **EN:** Zip layout:

```plaintext
\Noted\C\Users\Simon.stark\AppData\Roaming\Notepad++
```

> **ES:** Archivos obtenidos: / **EN:** Files obtained:

```plaintext
D:.
│  config.xml
│  session.xml
│
└─backup
        LootAndPurge.java@2023-07-24_145332
        YOU HAVE BEEN HACKED.txt@2023-07-24_150548
```

> **ES:** Registro en `config.xml`: / **EN:** Record in `config.xml`:

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<NotepadPlus>
    <FindHistory nbMaxFindHistoryPath="10" nbMaxFindHistoryFilter="10" nbMaxFindHistoryFind="10" nbMaxFindHistoryReplace="10" matchWord="no" matchCase="no" wrap="yes" directionDown="yes" fifRecuisive="yes" fifInHiddenFolder="no" fifProjectPanel1="no" fifProjectPanel2="no" fifProjectPanel3="no" fifFilterFollowsDoc="no" fifFolderFollowsDoc="no" searchMode="0" transparencyMode="1" transparency="150" dotMatchesNewline="no" isSearch2ButtonsMode="no" regexBackward4PowerUser="no" bookmarkLine="no" purge="no" />
    <History nbMaxFile="10" inSubMenu="no" customLength="-1">
        <File filename="C:\Program Files\Notepad++\change.log" />
        <File filename="C:\Users\Simon.stark\Documents\Internal-DesktopApp\Prototype-Internal_Login.cs" />
        <File filename="C:\Users\Simon.stark\Documents\Dev-WebServer-BetaProd\dev2prod_fileupload.php" />
        <File filename="C:\Users\Simon.stark\Documents\Internal-DesktopApp\App_init_validation.yml" />
        <File filename="C:\Users\Simon.stark\Documents\Dev_Ops\AWS_objects migration.pl" />
```

```plaintext title="Answer"
C:\Users\Simon.stark\Documents\Dev_Ops\AWS_objects migration.pl
```

## Task 2 — Fuente del recolector Java / Java collector source

> [ZH] "攻击者复制了一些程序代码并在系统上对其进行了编译……该代码收集了敏感数据并为其外泄做好了准备。该程序源文件的完整路径是什么？"
> **ES:** El atacante compiló código en el sistema (living-off-the-land, víctima ingeniera) para recolectar y preparar datos: ¿ruta completa del fuente?
> **EN:** The attacker compiled code on-box (living-off-the-land, victim is an engineer) to collect and stage data: what is the full source path?

> **ES:** Revisar `session.xml` → pestañas abiertas y sus `backupFilePath`.
> **EN:** Check `session.xml` → open tabs and their `backupFilePath`.

> **ES:** Contenido de `session.xml`: / **EN:** `session.xml` contents:

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<NotepadPlus>
    <Session activeView="0">
        <mainView activeIndex="1">
            <File firstVisibleLine="21" xOffset="0" scrollWidth="848" startPos="1697" endPos="1697" selMode="0" offset="0" wrapCount="1" lang="Java" encoding="-1" userReadOnly="no" filename="C:\Users\Simon.stark\Desktop\LootAndPurge.java" backupFilePath="C:\Users\Simon.stark\AppData\Roaming\Notepad++\backup\LootAndPurge.java@2023-07-24_145332" originalFileLastModifTimestamp="-1354503710" originalFileLastModifTimestampHigh="31047188" tabColourId="-1" mapFirstVisibleDisplayLine="-1" mapFirstVisibleDocLine="-1" mapLastVisibleDocLine="-1" mapNbLine="-1" mapHigherPos="-1" mapWidth="-1" mapHeight="-1" mapKByteInDoc="512" mapWrapIndentMode="-1" mapIsWrap="no" />
            <File firstVisibleLine="0" xOffset="0" scrollWidth="1072" startPos="672" endPos="672" selMode="0" offset="0" wrapCount="1" lang="None (Normal Text)" encoding="-1" userReadOnly="no" filename="C:\Users\Simon.stark\Desktop\YOU HAVE BEEN HACKED.txt" backupFilePath="C:\Users\Simon.stark\AppData\Roaming\Notepad++\backup\YOU HAVE BEEN HACKED.txt@2023-07-24_150548" originalFileLastModifTimestamp="1536217129" originalFileLastModifTimestampHigh="31047190" tabColourId="-1" mapFirstVisibleDisplayLine="-1" mapFirstVisibleDocLine="-1" mapLastVisibleDocLine="-1" mapNbLine="-1" mapHigherPos="-1" mapWidth="-1" mapHeight="-1" mapKByteInDoc="512" mapWrapIndentMode="-1" mapIsWrap="no" />
        </mainView>
        <subView activeIndex="0" />
    </Session>
</NotepadPlus>
```

```plaintext title="Answer"
C:\Users\Simon.stark\Desktop\LootAndPurge.java
```

## Task 3 — Archivo final a exfiltrar / Final staged archive

> [ZH] "包含所有要外泄的数据的最终存档文件的文件名是什么？"
> **ES:** ¿Cómo se llama el archivo final con todos los datos a exfiltrar?
> **EN:** What is the filename of the final archive holding all data to exfiltrate?

> **ES:** Leer el backup `LootAndPurge.java@2023-07-24_145332` → variables `zipFilePath` y `password`.
> **EN:** Read the backup `LootAndPurge.java@2023-07-24_145332` → `zipFilePath` and `password` variables.

> **ES:** Código fuente en el backup: / **EN:** Source code in the backup:

```java
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.zip.ZipEntry;
import java.util.zip.ZipOutputStream;

public class Sensitive_data_extort {
    public static void main(String[] args) {
        String username = System.getProperty("user.name");
        String desktopDirectory = "C:\\Users\\" + username + "\\Desktop\\";
        List<String> extensions = Arrays.asList("zip", "docx", "ppt", "xls", "md", "txt", "pdf");
        List<File> collectedFiles = new ArrayList<>();

        collectFiles(new File(desktopDirectory), extensions, collectedFiles);

        String zipFilePath = desktopDirectory + "Forela-Dev-Data.zip";
        String password = "sdklY57BLghvyh5FJ#fion_7";

        createZipArchive(collectedFiles, zipFilePath, password);

        System.out.println("Zip archive created successfully at:" + zipFilePath);
    }

    private static void collectFiles(File directory, List<String> extensions, List<File> collectedFiles) {
        File[] files = directory.listFiles();
        if (files != null) {
            for (File file : files) {
                if (file.isDirectory()) {
                    collectFiles(file, extensions, collectedFiles);
                } else {
                    String fileExtension = getFileExtension(file.getName());
                    if (extensions.contains(fileExtension)) {
                        collectedFiles.add(file);
                    }
                }
            }
        }
    }


    private static String getFileExtension(String fileName) {
        int dotIndex = fileName.lastIndexOf(".");
        if (dotIndex> 0 && dotIndex < fileName.length() - 1) {
            return fileName.substring(dotIndex + 1).toLowerCase();
        }
        return "";
    }

    private static void createZipArchive(List<File> files, String zipFilePath, String password) {
        byte[] buffer = new byte[1024];

        try (ZipOutputStream zipOutputStream = new ZipOutputStream(new FileOutputStream(zipFilePath))) {
            zipOutputStream.setMethod(ZipOutputStream.DEFLATED);
            zipOutputStream.setComment("Forela-Dev-Data.zip");
            zipOutputStream.setPassword(password.toCharArray());

            for (File file : files) {
                FileInputStream fileInputStream = new FileInputStream(file);
                zipOutputStream.putNextEntry(new ZipEntry(file.getName()));

                int length;
                while ((length = fileInputStream.read(buffer)) > 0) {
                    zipOutputStream.write(buffer, 0, length);
                }

                zipOutputStream.closeEntry();
                fileInputStream.close();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

```plaintext title="Answer"
Forela-Dev-Data.zip
```

## Task 4 — Última modificación UTC / Last modification UTC

> [ZH] "攻击者最后修改程序源文件时的 UTC 时间戳是什么？"
> **ES:** ¿Cuál es el timestamp UTC de la última modificación del fuente?
> **EN:** What is the UTC timestamp of the last modification to the source file?

> **ES:** Tomar `originalFileLastModifTimestamp` + `...High` de `session.xml` (FILETIME) y convertir desde 1601-01-01 (ver enlace comunidad Notepad++).
> **EN:** Take `originalFileLastModifTimestamp` + `...High` from `session.xml` (FILETIME) and convert from 1601-01-01 (see Notepad++ community link).

> **ES:** Datos de la Task 2: / **EN:** Data from Task 2:

```plaintext
backupFilePath="C:\Users\Simon.stark\AppData\Roaming\Notepad++\backup\LootAndPurge.java@2023-07-24_145332"
originalFileLastModifTimestamp="-1354503710"
originalFileLastModifTimestampHigh="31047188"
```

> **ES:** Según la comunidad Notepad++: / **EN:** Per the Notepad++ community:

[Need Explanation of a few Session.xml Parameters & Values | Notepad++ Community](https://community.notepad-plus-plus.org/topic/22662/need-explanation-of-a-few-session-xml-parameters-values)

> **ES:** Cálculo con script: / **EN:** Compute with script:

```python
import datetime

timestamp_low = -1354503710
timestamp_high = 31047188

full_timestamp = (timestamp_high << 32) | (timestamp_low & 0xFFFFFFFF)

timestamp_seconds = full_timestamp / 10**7
timestamp = datetime.datetime(1601, 1, 1) + datetime.timedelta(seconds=timestamp_seconds)

print(timestamp)
# 2023-07-24 09:53:23.322723
```

```plaintext title="Answer"
2023-07-24 09:53:23
```

## Task 5 — Wallet del rescate / Ransom wallet

> [ZH] "攻击者在窃取数据后写了一份数据勒索信。攻击者要求付款的加密钱包地址是什么？"
> **ES:** Tras robar datos dejó nota de extorsión: ¿qué wallet exige para el pago?
> **EN:** After stealing data he left an extortion note: which wallet does he demand payment to?

> **ES:** Leer el backup `YOU HAVE BEEN HACKED.txt@2023-07-24_150548` → enlaces paste protegidos; reutilizar el `password` del fuente como clave.
> **EN:** Read the backup `YOU HAVE BEEN HACKED.txt@2023-07-24_150548` → password-gated paste links; reuse the source `password` as the key.

> **ES:** Contenido del backup de la nota: / **EN:** Note backup contents:

```plaintext
HEllo

This note is placed in your desktop and copied to other locations too. You have been hacked and your data has been deleted from your
system. We made copies of your sensitive data and uploaded to our servers. The rule is simple

                                                       YOU PAY US
                                                           AND
                         WE DO NOT RELEASE YOUR COMPANY SECRETS TO PUBLIC AND RETURN YOUR DATA SAFELY TO YOU


Failiure to oblige will result in immediate data leak to the public.

For detailed information and process , Visit below link

https://pastebin.com/CwhBVzPq

OR

https://pastes.io/mvc6sue6cf
```

> **ES:** Los enlaces exigen contraseña; el fuente trae una (`password`): / **EN:** The links require a password; the source carries one (`password`):

```java
String password = "sdklY57BLghvyh5FJ#fion_7";
```

> **ES:** Esa clave desbloquea el pago: / **EN:** That key unlocks the payment details:

```plaintext
If you are here then you know that you have no other choice than to pay us.Your Sensitive DATA is in our hands and we WILL release it to PUBLIC By midnight if you don't pay us a ransom.

We Want 50000e $ in ETH currency by midnight. This amount is very reasonable as we know FORELA is a multi million dollar company, but since we were able to extort small amount of data , this is our final offer.

Ethereum Wallet: 0xca8fa8f0b631ecdb18cda619c4fc9d197c8affca

Person of contact : CyberJunkie@mail2torjgmxgexntbrmhvgluavhj7ouul5yar6ylbvjkxwqf6ixkwyd.onion
```

```plaintext title="Answer"
0xca8fa8f0b631ecdb18cda619c4fc9d197c8affca
```

## Task 6 — Email de contacto / Contact email

> [ZH] "联系支持人员的电子邮件地址是什么？"
> **ES:** ¿Cuál es la dirección de contacto/soporte?
> **EN:** What is the contact/support email address?

> **ES:** Mismo contenido desbloqueado de la Task 5 (persona de contacto).
> **EN:** Same unlocked content as Task 5 (person of contact).

> **ES:** Ya aparece en la Task anterior. / **EN:** Already shown in the previous task.

```plaintext title="Answer"
CyberJunkie@mail2torjgmxgexntbrmhvgluavhj7ouul5yar6ylbvjkxwqf6ixkwyd.onion
```

## Fuentes / Sources

- Dificultad y categoria: [momenbasel/htb-writeups - Sherlocks index](https://github.com/momenbasel/htb-writeups/blob/main/sherlocks/README.md) - fecha de acceso: 2026-09-24.
- Autor notas: Apuromafo.

---

## ⚠️ Aviso Legal / Disclaimer

> **ES:** Uso educativo y personal únicamente. No afiliado a HackTheBox. Evidencia y respuestas con contexto, no solo la respuesta suelta.
> **EN:** Educational and personal use only. Not affiliated with HackTheBox. Evidence and contextual answers, not bare answers.

_Fecha de edición: 2026-09-24_
