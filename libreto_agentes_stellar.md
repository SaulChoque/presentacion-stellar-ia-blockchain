# 🎃 Libreto v2: Agentes en la Red Stellar
### *"Blockchain sin misterio: redes, transacciones y ecosistema"*
**Evento:** AI Agents + Blockchain Halloween · [Luma](https://luma.com/742fo5f8)
**Charla #03 · Duración: 25–30 min · Público: Estudiantes de Informática**

> [!NOTE]
> **Sincronizado con el deck** (`dist/slides.js`, 18 slides): títulos, subtítulos, visuales y textos de cada slide son los que aparecen en pantalla. Las **slides 2 a 9 son interactivas** (21 sub-slides repartidos, 67 pasos) y se controla también desde `/?notes`. Los ajustes técnicos de contenido están en `dist/revision.md`.

---

> [!NOTE]
> **Ajuste de enfoque:** Los expositores anteriores ya habrán explicado qué son los agentes de IA.
> Esta charla arranca desde ahí y se enfoca en: **¿por qué Stellar? ¿cómo funciona? ¿cómo un agente opera en ella?**
> El nivel técnico puede ser mayor — son estudiantes de informática.

> [!IMPORTANT]
> **Temática: M3GAN** — ícono tech-horror viral de Halloween 2026. M3GAN *es* un agente autónomo.
> Se usa como hilo conductor, no como explicación de agentes (eso ya está cubierto).

---

## 🗂️ Estructura General

| # | Sección | Duración | Slides |
|---|---------|----------|--------|
| 0 | **Hook M3GAN + puente con charlas anteriores** | 2 min | 1 |
| 1 | **Blockchain para informáticos** | 6 min | 2–5 |
| 2 | **Stellar: arquitectura y por qué importa** | 8 min | 6–10 |
| 3 | **Cómo un agente opera en Stellar** | 9 min | 11–15 |
| 4 | **Demo / Casos reales** | 3 min | 16–17 |
| 5 | **Cierre M3GAN** | 2 min | 18 |

---

## 🎬 SECCIÓN 0 — HOOK (2 min)

### 🖥️ Slide 1
> **Antetítulo:** "Los agentes han despertado."
> **Título:** "Esta noche le damos billetera."
> **Subtítulo:** *"Ya saben qué es un agente. Ahora, ¿cómo maneja dinero?"*
> **Etiqueta:** UNA HISTORIA DE AGENTES & BLOCKCHAIN
> **Escena:** muñeca gótica de cabello plateado, luna, calabaza, fantasma-robot con sombrero, billetera de papel y murciélago.
> **Apoyo:** *"M3GAN puede decidir. Hoy descubrimos cómo puede pagar."*

---

### 📜 Libreto

**"Mis colegas ya les explicaron qué es un agente de IA. Ya tienen claro que puede percibir, razonar y actuar de forma autónoma."**

**"Yo vengo a responder la siguiente pregunta: si un agente puede hacer todo eso… ¿cómo maneja dinero? ¿Cómo paga servicios? ¿Cómo cobra por su trabajo?"**

**"¿Y por qué una blockchain, específicamente Stellar, es la respuesta?"**

**"Para darle contexto, piensen en M3GAN — la IA agente más famosa del pop culture actual. M3GAN puede cuidar a una niña, detectar amenazas, tomar decisiones. Pero si quisiera comprar algo en internet… no tiene cómo. No tiene cuenta bancaria. No tiene DNI."**

**"Hoy vemos cómo Stellar le da la billetera que le faltaba. Y lo que eso significa para el futuro del software autónomo."**

> 🎙️ **Tip:** Tono directo, sin dramatismo exagerado — son informáticos, aprecian ir al grano. El hook de M3GAN es el guiño de humor, no el foco principal.

---

## ⛓️ SECCIÓN 1 — Blockchain para informáticos (6 min)

> [!NOTE]
> No es una explicación básica "para abuelas". El público ya sabe de estructuras de datos,
> redes y criptografía básica. Habla con esas palabras.

> [!NOTE]
> **Slides 2 a 9 son interactivas.** Cada slide "padre" contiene sub-slides (`dist/acto2.html`) y siguen el orden del libreto. Con `→` (o el botón → de `/?notes`) avanza un sub-paso; al terminar los pasos de la slide pasa a la siguiente. `←` retrocede. En `/?notes` el panel **"Sub-slides de la slide N · en vivo"** tiene ◀ ▶, salto directo a cualquier paso y botones de interacción que se replican en la pantalla principal. (`Espacio` inicia/pausa el reloj, no avanza.)

| Slide padre | Sub-slides | Pasos | Se dice… |
|--|--|--|--|
| **2** · Una estructura que ya conoces | 1 Lista enlazada por hashes · 2 Una red distribuida | 3 + 3 = 6 | Intro de linked list + "La diferencia clave…" |
| **3** · Dentro de un bloque | 3 Anatomía (grimorio) · 4 Muchas transacciones, una huella · 5 Árbol de Merkle · 6 La firma autoriza el bloque | 5 + 3 + 3 + 3 = 14 | "Cada bloque tiene…" + "¿Por qué el árbol de Merkle?" |
| **4** · Cambias un dato. Rompes la cadena | 7 Inmutabilidad por encadenamiento | 3 | "La inmutabilidad sale de esto…" |
| **5** · ¿Quién decide qué es válido? | 8 Tres modelos de consenso · 9 SCP y quórums | 3 + 3 = 6 | "Ahora, el mecanismo de consenso…" + "Stellar usa algo diferente…" |
| **6** · El consenso es un acuerdo | 10 Cada nodo elige en quién confía · 11 Los quórums se superponen · 12 Sin reorganizaciones | 3 + 3 + 3 = 9 | "SCP fue diseñado por David Mazières…" |
| **7** · Una dirección. Muchos activos | 13 Un par de claves · 14 Una cuenta, muchos activos · 15 El sequence number | 3 + 3 + 3 = 9 | "Las cuentas en Stellar usan criptografía de curva elíptica…" |
| **8** · Los verbos de Stellar | 16 Los verbos · 17 Una transacción, varias operaciones · 18 Todo o nada | 5 + 3 + 3 = 11 | "Las interacciones con la red se hacen mediante operaciones…" |
| **9** · Reglas que ejecuta la red | 19 Del código al ledger · 20 Un sandbox dentro de la red · 21 Reglas para agentes | 3 + 3 + 3 = 9 | "Y desde 2023 Stellar tiene Soroban…" |

---

### 🖥️ Slide 2 — "Una estructura que ya conoces." (6 pasos)
> **Subtítulo:** *Una lista enlazada, distribuida y verificable.*

| Sub-slide | Título en pantalla | Qué ocurre | Interacción desde notas |
|--|--|--|--|
| 1 · Lista enlazada por hashes (3) | "Cada bloque recuerda al anterior." | Bloque 01 → 02 → 03; aparecen los enlaces y "EL HASH ENLAZA →" | Bloque 1 / 2 / 3 |
| 2 · Una red distribuida (3) | "No vive en una sola computadora." | **1** cinco nodos, cada uno con la misma cadena · **2** un nodo propone el bloque 04 y se difunde · **3** los nodos votan; con la mayoría el bloque 04 queda en todas las copias | ↺ Repetir animación |

> **Cuidado:** no digas que siempre vota la mayoría de nodos; cada red tiene su propio consenso. Los nodos pueden acordar un historial válido sin tener copias exactamente idénticas en el mismo instante.

---

### 🖥️ Slide 3 — "Dentro de un bloque." (14 pasos)
> **Subtítulo:** *El hash conecta. Las firmas autorizan.*

| Sub-slide | Título en pantalla | Qué ocurre | Interacción desde notas |
|--|--|--|--|
| 3 · Anatomía de un bloque (5) | "Dentro de un bloque." | El grimorio muestra el bloque línea a línea; luego se resalta `prev_hash`, `timestamp`, `merkle_root` y `nonce / validator_sig`, uno por paso | Los 4 campos |
| 4 · Muchas transacciones, una huella (3) | "Muchas transacciones. Una huella." | Aparece la lista de transacciones, crece a cientos y se resume con un hash en `merkle_root` | ↺ Repetir animación |
| 5 · Árbol de Merkle (3) | "Verifica sin leerlo todo." | Raíz, H(AB), H(CD) y TX 01–04; se ilumina la ruta de la prueba | TX 01 – TX 04 |
| 6 · La firma autoriza el bloque (3) | "La firma autoriza el bloque." | El validador firma el encabezado con su clave privada; tres nodos verifican con la clave pública. Alterar el timestamp rompe la firma | ⚡ Alterar / restaurar bloque |

> **Cuidado:** es un bloque didáctico, no el header de Stellar. Los hashes son ilustrativos, no un SHA-256 en vivo.
> **Referencia del bloque** (modelo conceptual):
> ```
> ┌─────────────────────────────────┐
> │  Block Header                   │
> │  ├─ prev_hash: 0xA3F2…          │
> │  ├─ timestamp: 1730150400       │
> │  ├─ merkle_root: 0x9C1D…        │
> │  └─ nonce / validator_sig       │
> ├─────────────────────────────────┤
> │  Transactions []                │
> │  ├─ tx_0: Alice → Bob 10 XLM    │
> │  ├─ tx_1: Bob → Carol 5 XLM     │
> │  └─ ...                         │
> └─────────────────────────────────┘
> ```

---

### 🖥️ Slide 4 — "Cambias un dato. Rompes la cadena." (3 pasos)
> **Subtítulo:** *Los hashes detectan cambios; el consenso protege la historia.*

| Sub-slide | Título en pantalla | Qué ocurre | Interacción desde notas |
|--|--|--|--|
| 7 · Inmutabilidad por encadenamiento (3) | "Cambia uno. Se nota en todos." | Bloques 01–04; al alterar el 02 su hash cambia y el 03 y el 04 se marcan en rojo | Alterar / restaurar bloque 02 |

> **Texto:** *"Cambiar un bloque rompe la cadena. La red lo detecta y lo rechaza."*
> **Cuidado:** no afirmes que sea matemáticamente imposible ni que baste el 51 % de los nodos. En Bitcoin el 51 % se refiere al poder de hash.

---

### 🖥️ Slide 5 — "¿Quién decide qué es válido?" (6 pasos)
> **Subtítulo:** *Distintas redes. Distintos modelos de confianza.*

| Sub-slide | Título en pantalla | Qué ocurre | Interacción desde notas |
|--|--|--|--|
| 8 · Tres modelos de consenso (3) | "¿Cómo se ponen de acuerdo?" | Bitcoin PoW · Ethereum PoS · Stellar SCP | Las tres tarjetas |
| 9 · SCP y quórums (3) | "La confianza crea acuerdo." | Quórums superpuestos y simulación de acuerdo | Simular / reiniciar acuerdo |

> **Cuidado:** no compares segundos de bloque con segundos de finalidad (los slots de 12 s de Ethereum no son finalidad inmediata). Stellar cierra acuerdos en unos 5 segundos aproximadamente.
> **Referencia comparativa:**
>
> | Mecanismo | Quién valida | Costo energético | Velocidad |
> |--|--|--|--|
> | **PoW** · Bitcoin | Mineros (CPU/GPU) | 🔥🔥🔥 Alto | ~10 min |
> | **PoS** · Ethereum | Validadores con stake | 🔥 Medio | ~15 seg |
> | **SCP** · Stellar | Quórum de nodos de confianza | ✅ Mínimo | **3–5 seg** |

---

### 📜 Libreto

**"Para los que ya tienen bases de estructuras de datos: una blockchain es esencialmente una linked list. Cada nodo tiene un puntero al anterior — solo que aquí el 'puntero' es el hash criptográfico del bloque previo."**

*[señalar slide 2]*

**"La diferencia clave con una lista enlazada normal es que esta lista vive en miles de computadoras simultáneamente, y cada nodo de la red tiene una copia idéntica. Para agregar un bloque, la mayoría de la red debe estar de acuerdo."**

*[señalar slide 3]*

**"Cada bloque tiene: el hash del bloque anterior —que es lo que crea la cadena—, un timestamp, la raíz de un árbol de Merkle con todas las transacciones, y la firma del validador."**

**"¿Por qué el árbol de Merkle? Porque permite verificar que una transacción específica está incluida en el bloque sin descargar el bloque completo. Eficiencia."**

*[señalar slide 4]*

**"La inmutabilidad sale de esto: si cambias una transacción en el bloque 2, el hash del bloque 2 cambia. Eso invalida el hash en el bloque 3. Y en el 4. Y en el 5. La cadena se rompe. La red detecta la inconsistencia y rechaza esa versión."**

**"Para reescribir la historia, un atacante tendría que rehacer los bloques posteriores y lograr que la red acepte esa versión — algo que las reglas de consenso hacen extremadamente costoso. En Bitcoin se habla del 51 %, pero eso mide poder de cómputo, no cantidad de nodos."**

*[señalar slide 5]*

**"Ahora, el mecanismo de consenso es donde las blockchains se diferencian. Bitcoin usa Proof of Work — competencia de cómputo brutal, energéticamente costosa. Ethereum usa Proof of Stake — mejor, pero sigue siendo lento para micropagos."**

**"Stellar usa algo diferente: el Stellar Consensus Protocol, o SCP. En vez de competir, los nodos definen 'quórums de confianza' — conjuntos de nodos en los que confían. El consenso emerge de esos quórums superpuestos. El resultado: finalidad en 3 a 5 segundos, con costo computacional mínimo."**

**"Ya entraremos al detalle de SCP. Primero entendamos por qué Stellar en particular."**

> 🎙️ **Tip:** Puedes preguntar rápido: *"¿Cuántos ya habían escuchado de Merkle trees?"* — conecta con lo que ya saben. No te extiendas en la teoría de consenso todavía, solo siembra la curiosidad para el siguiente bloque.

---

## ⭐ SECCIÓN 2 — Stellar: arquitectura y por qué importa (8 min)

### 🖥️ Slide 6 — "El consenso es un acuerdo."
> **Subtítulo:** *SCP · Federated Byzantine Agreement*

| Sub-slide | Título en pantalla | Qué ocurre | Interacción desde notas |
|--|--|--|--|
| 10 · Cada nodo elige en quién confía (3) | "Cada nodo elige en quién confía." | Nodo A y su quorum slice { B, C }; sus votos le bastan para avanzar | ↺ Repetir animación |
| 11 · Los quórums se superponen (3) | "Los quórums se superponen." | Dos quórums comparten el nodo C; esa intersección evita historias opuestas | ↺ Repetir animación |
| 12 · Sin reorganizaciones (3) | "Sin reorganizaciones." | Nominar → votar → cerrar, en unos 5 segundos y sin forks | ↺ Repetir animación |
> **Visual:** cuatro sigilos **Nodo A · B · C · D** con la nota *"Quórums de confianza superpuestos"*.
> **Frase de apoyo:** *"No hay un líder. No hay mineros. Solo acuerdo matemático entre nodos de confianza."*

---

### 🖥️ Slide 7 — "Una dirección. Muchos activos."
> **Subtítulo:** *La clave privada permanece fuera del ledger.*

| Sub-slide | Título en pantalla | Qué ocurre | Interacción desde notas |
|--|--|--|--|
| 13 · Un par de claves (3) | "Un par de claves." | Clave privada → pública (Ed25519); la privada firma, la pública verifica | ↺ Repetir animación |
| 14 · Una cuenta, muchos activos (3) | "Una cuenta, muchos activos." | XLM, luego USDC y MY_TOKEN, cada uno tras su `ChangeTrust` | ↺ Repetir animación |
| 15 · El sequence number (3) | "Ni una vez más." | La transacción se acepta y el número avanza; reenviarla se rechaza | ↺ Repetir animación |
> **Visual:** libro de notas con la cuenta Stellar:
> ```
> Account {
>   public_key: "GABC…XYZ",
>   balances: [ XLM, USDC, MY_TOKEN:GISSUER ],
>   sequence_number: 12345678
> }
> // Clave privada: en el firmante, nunca on-chain
> // Los activos emitidos requieren trustline
> ```

---

### 🖥️ Slide 8 — "Los verbos de Stellar."
> **Subtítulo:** *Operaciones agrupadas: todo ocurre, o nada ocurre.*

| Sub-slide | Título en pantalla | Qué ocurre | Interacción desde notas |
|--|--|--|--|
| 16 · Los verbos de Stellar (5) | "Los verbos de Stellar." | Una tarjeta por paso: `Payment`, `ChangeTrust`, `ManageSellOffer`, `InvokeHostFunction`, `SetOptions` | — |
| 17 · Una transacción, varias operaciones (3) | "Una transacción, varias operaciones." | Tres `Payment` dentro de una transacción; una sola firma; se envía a la red como paquete | ↺ Repetir animación |
| 18 · Todo o nada (3) | "Todo o nada." | Las operaciones esperan, todas se aplican (✓) y en el caso de fallo ninguna se aplica (↩ revertida) | ↺ Repetir animación |
> **Visual:** tabla de operaciones:
>
> | Operación | Propósito |
> |--|--|
> | `Payment` | Enviar un activo |
> | `ChangeTrust` | Aceptar un activo emitido |
> | `ManageSellOffer` | Crear una oferta en el DEX |
> | `InvokeHostFunction` | Invocar un contrato Soroban |
> | `SetOptions` | Configurar firmas y umbrales |
>
> **Nota:** *Varias operaciones pueden agruparse en una sola transacción. Atómicas.*

---

### 🖥️ Slide 9 — "Reglas que ejecuta la red."
> **Subtítulo:** *Soroban · Rust → WebAssembly*

| Sub-slide | Título en pantalla | Qué ocurre | Interacción desde notas |
|--|--|--|--|
| 19 · Del código al ledger (3) | "Del código al ledger." | Contrato en Rust → compilado a WebAssembly (`contrato.wasm`) → desplegado en el ledger de Stellar | ↺ Repetir animación |
| 20 · Un sandbox dentro de la red (3) | "Un sandbox dentro de la red." | El contrato corre en un sandbox WASM; misma entrada, misma salida; tres nodos obtienen el mismo resultado | ↺ Repetir animación |
| 21 · Reglas para agentes (3) | "Reglas que el agente no puede saltar." | Un pago a un destino aprobado pasa; a uno desconocido el contrato lo rechaza; reglas on-chain auditables | ↺ Repetir animación |

> **Cuidado:** Rust ayuda a evitar errores de memoria y WASM es determinista, pero ninguno garantiza que el contrato no tenga bugs: hay que auditarlo.
> **Visual:** tres piezas apiladas:
> ```
> ┌──────────────────────────────┐
> │   Contrato en Rust           │  ← Tu lógica de negocio
> ├──────────────────────────────┤
> │   WebAssembly                │  ← Ejecución controlada
> ├──────────────────────────────┤
> │   Stellar Ledger             │  ← Estado compartido
> └──────────────────────────────┘
> ```
> **Texto:** *"Contratos en Rust → compilados a WASM → ejecutados on-chain. Deterministas, auditables."*

---

### 🖥️ Slide 10 — "Diseñado para mover valor."
> **Subtítulo:** *Pagos programables como parte de tu software.*
> **Visual:** tres lápidas:
> - **Segundos** — Cierre de ledger
> - **100 stroops** — Mínimo por operación clásica\*
> - **USDC** — Emitido por Circle en Stellar
>
> *\*Mínimo clásico sin congestión. Soroban añade tarifas por recursos.*
> **Revisión:** no se muestran cifras de throughput ni de adopción porque no están comprobadas; si las mencionas en voz alta, cita fuente.

---

### 📜 Libreto

**"Vamos con Stellar en detalle. Lo primero que necesitan entender es SCP — el Stellar Consensus Protocol."**

*[señalar slide 6]*

**"SCP fue diseñado por David Mazières, el mismo investigador detrás de varios trabajos de sistemas distribuidos en Stanford. La idea central es el 'Federated Byzantine Agreement'."**

**"En vez de requerir que toda la red acuerde antes de confirmar una transacción — lo cual es lento — cada nodo define su propio 'quórum slice': el conjunto mínimo de nodos en los que confía. El consenso emerge cuando los quórums se superponen suficientemente."**

**"El resultado práctico: transacciones con finalidad en 3 a 5 segundos. Sin rollbacks. Sin reorganizaciones de cadena como en Bitcoin. Una vez confirmado, está confirmado."**

*[señalar slide 7]*

**"Las cuentas en Stellar usan criptografía de curva elíptica — Ed25519. Una cuenta es un par de claves: la clave pública es tu dirección en la red, la privada firma las transacciones. Nada nuevo para ustedes conceptualmente."**

**"Lo interesante es que una cuenta puede tener balances en múltiples assets simultáneamente: XLM que es el token nativo, USDC, o cualquier token personalizado que alguien haya emitido. Stellar tiene un sistema de assets nativos muy flexible."**

**"El sequence number en cada cuenta evita replay attacks — una transacción solo puede ejecutarse una vez. Clásico."**

*[señalar slide 8]*

**"Las interacciones con la red se hacen mediante operaciones. Varias operaciones pueden agruparse en una sola transacción y son atómicas — o todas se ejecutan, o ninguna. Eso es crítico para agentes: si un agente necesita hacer 3 pagos encadenados, o salen los tres o no sale ninguno."**

*[señalar slide 9]*

**"Y desde 2023 Stellar tiene Soroban — su sistema de smart contracts. Los contratos se escriben en Rust, se compilan a WebAssembly, y se ejecutan en un sandbox dentro de la red. Rust porque garantiza ausencia de bugs de memoria. WASM porque es determinista — el mismo input siempre da el mismo output en cualquier nodo."**

**"Para agentes esto es clave: pueden interactuar con contratos que definen reglas de negocio complejas, inmutables y verificables."**

*[señalar slide 10]*

**"¿Por qué Stellar y no Ethereum, Solana, o cualquier otra? Tres razones prácticas para agentes:"**

**"Uno — velocidad con finalidad real. 3 a 5 segundos y ya. En Ethereum puedes tener reorganizaciones de cadena. Un agente no puede operar bien con incertidumbre sobre si su transacción es definitiva."**

**"Dos — fees predecibles y microscópicos. Un agente puede hacer miles de micropagos al día. Si cada pago cuesta un dólar en gas, el modelo de negocio no funciona. En Stellar el costo es prácticamente cero."**

**"Tres — USDC nativo. Sin bridges, sin tokens envueltos que puedan perder el peg. Los agentes operan con USDC directamente en la red Stellar, emitido por Circle."**

> 🎙️ **Tip:** El slide de SCP es técnico — si el tiempo aprieta, simplifícalo a "es un protocolo de consenso basado en quórums de confianza, más eficiente que PoW y PoS". No te pierdas en la teoría. Lo importante es el *resultado*: 3-5 segundos, barato. El resto es profundidad opcional.

---

## 🤖 SECCIÓN 3 — Cómo un agente opera en Stellar (9 min)

### 🖥️ Slide 11 — "El software también necesita pagar."
> **Subtítulo:** *M3GAN puede razonar. El banco espera una persona.*
> **Visual:** dos tarjetas contrapuestas:
> - **Sistema tradicional** — Identidad legal · cuenta bancaria
> - **Identidad on-chain** — Claves · firma · saldo
> **Texto:** *"No tienen DNI. No pueden abrir cuenta bancaria. El sistema financiero tradicional no fue diseñado para software autónomo."*

---

### 🖥️ Slide 12 — "Una wallet comienza con claves."
> **Subtítulo:** *Generar claves no activa una cuenta: hay que fondearla.*
> **Visual:** snippet en el grimorio (aparece línea a línea):
> ```python
> from stellar_sdk import Keypair, Server
>
> agent = Keypair.random()
> print(agent.public_key)
>
> # Guardar agent.secret fuera del código y del LLM
> # Fondear en testnet con Friendbot
> server = Server("https://horizon-testnet.stellar.org")
> ```

---

### 🖥️ Slide 13 — "De la decisión al pago."
> **Subtítulo:** *La construcción y la firma ocurren en el cliente.*
> **Visual:** flujo de 4 pasos:
> 1. **SDK** — Cargar cuenta y construir
> 2. **Firmante** — Autorizar y firmar localmente
> 3. **Horizon** — Enviar la transacción
> 4. **Red Stellar** — Validar, acordar y confirmar

---

### 🖥️ Slide 14 — "HTTP 402: una API que cobra."
> **Subtítulo:** *x402 · flujo conceptual, requiere integración compatible.*
> **Visual:** flujo de 4 pasos:
> 1. **GET /recurso** — El agente solicita datos
> 2. **402 · PAYMENT-REQUIRED** — El servidor indica condiciones
> 3. **PAYMENT-SIGNATURE** — El cliente firma y reintenta
> 4. **200 · Recurso** — Verificación y liquidación del pago
> **Nota:** *"El código HTTP 402 existe desde los primeros estándares de HTTP. Esperó décadas para que las máquinas lo usaran."*

---

### 🖥️ Slide 15 — "Autonomía con límites."
> **Subtítulo:** *Un contrato puede hacer cumplir un presupuesto.*
> **Visual:** pseudocódigo (no es un contrato desplegable):
> ```
> require_auth(agente)
> assert(amount > 0)
> assert(spent_today + amount <= daily_limit)
> update_spent_today(amount)
> transfer(to, amount)
>
> // Custodia, permisos y upgrades también importan
> ```
> **Texto:** *"Las reglas del agente pueden ser código on-chain. Verificables, sin depender de una promesa."*

---

### 📜 Libreto

**"Tenemos blockchain. Tenemos Stellar. Ahora viene la parte interesante: cómo un agente de IA realmente opera en esta red."**

*[señalar slide 11]*

**"El primer obstáculo es de identidad. Un agente no puede entrar a un banco y abrir cuenta. El sistema financiero tradicional está construido para personas jurídicas o naturales — no para procesos de software."**

**"Stellar lo resuelve en tres líneas de código."**

*[señalar slide 12 — aparece línea a línea]*

**"Con el SDK de Python — o JavaScript, Go, Java, Rust, hay SDKs para todos — generas un keypair con `Keypair.random()`. Eso te da una clave pública y una privada. La pública es la dirección del agente en la red. La privada firma sus transacciones."**

**"Para activar la cuenta necesitas depositar el mínimo de reserva — 1 XLM actualmente, unos centavos. En testnet hay un 'friendbot' que lo hace gratis. En producción, el usuario que despliega el agente lo fondea."**

**"Y ya. El agente tiene identidad financiera en la red Stellar. Puede recibir fondos, puede enviar pagos, puede interactuar con contratos."**

*[señalar slide 13]*

**"Cuando el agente necesita hacer un pago, el flujo es así:"**

**"Construye una transacción con las operaciones que quiere ejecutar. La firma con su clave privada. La envía a través de la API de Horizon — el nodo de acceso a la red Stellar. Horizon la broadcast a la red. En 3 a 5 segundos, el protocolo SCP alcanza consenso y la transacción está confirmada."**

**"Todo programático. Todo sin intervención humana."**

*[señalar slide 14]*

**"Ahora el protocolo que más me gusta mencionar: x402."**

**"Cuando un agente quiere acceder a un recurso de pago en internet, hace un GET normal. El servidor responde con código 402 — Payment Required — y en el body incluye un objeto con: cuánto cobrar, en qué asset, a qué dirección, en qué red."**

**"El agente lee eso, firma y ejecuta el pago, y reintenta la solicitud con la prueba de pago en el header (en x402 v2: `PAYMENT-SIGNATURE`). El servidor verifica el pago y, si es válido, entrega el recurso."**

**"Todo esto ocurre en segundos, sin humanos, sin contratos firmados, sin subscripciones mensuales. Las máquinas se están pagando entre sí en tiempo real."**

**"El código 402 existe en HTTP desde sus primeros estándares, pensado para pagos que casi nadie usó en la web. x402 lo retoma para que las máquinas se paguen entre sí — hace falta que el servidor y el cliente soporten el protocolo."**

*[señalar slide 15]*

**"Y hay algo muy relevante para la confianza en sistemas autónomos: Soroban permite que las reglas bajo las cuales opera el agente sean código on-chain."**

**"Si le dices al usuario 'mi agente nunca va a gastar más de 10 USDC al día', eso puede estar codificado en un contrato inmutable en Stellar. No es una promesa. Es código que la red ejecuta."**

**"Para sistemas de producción donde un agente maneja fondos reales de usuarios, esto es la diferencia entre 'confíenme' y 'verifíquenlo ustedes mismos'. La auditoría es pública, permanente y sin intermediarios."**

> 🎙️ **Tip:** El slide de x402 es el más denso visualmente. Pasa por él despacio — es el momento más técnico y más impactante. Si ves que el tiempo se acaba, puedes recortar el slide 15 de Soroban a solo 1 minuto de mención rápida.

---

## 🌍 SECCIÓN 4 — Demo / Casos Reales (3 min)

### 🖥️ Slide 16 — "Del ecosistema a tu primer experimento."
> **Subtítulo:** *Distinguir productos existentes de ideas que puedes construir.*
> **Visual:** tres lápidas

**🏦 MoneyGram**
> Entrada y salida de efectivo con USDC en Stellar.

**📈 DEX nativo**
> Órdenes y automatización: un agente puede crear y cancelar ofertas por código.

**🧪 Testnet**
> Explora una transacción sin fondos reales: crea la cuenta, fóndea con Friendbot y míralo en el explorador.

---

### 🖥️ Slide 17 — "El stack completo."
> **Subtítulo:** *Cada capa tiene una responsabilidad.*
> **Visual:** diagrama de capas (de arriba a abajo)
> ```
> ┌─────────────────────────────────────────┐
> │   LLM / lógica del agente               │  ← Decide dentro de una política
> ├─────────────────────────────────────────┤
> │   SDK + firmante                        │  ← Construye, valida y autoriza
> ├─────────────────────────────────────────┤
> │   Horizon / Stellar RPC                 │  ← Acceso a la red según operación
> ├─────────────────────────────────────────┤
> │   Stellar + Soroban                     │  ← Consenso, estado y contratos
> └─────────────────────────────────────────┘
> ```

---

### 📜 Libreto

**"Tres ejemplos concretos de hoy, no del futuro."**

*[tarjeta por tarjeta]*

**"MoneyGram conecta efectivo y USDC en Stellar: el usuario puede entrar y salir de dólares digitales sin tener que entender la blockchain."**

**"El DEX nativo de Stellar permite crear y cancelar órdenes por código. Eso abre la puerta a agentes que automatizan estrategias, y los fees mínimos hacen viable operar con montos pequeños."**

**"Y para la demo, lo más honesto es Testnet: creas una cuenta, la fondeas con Friendbot y muestras la transacción en el explorador. Sin fondos reales, con todo el flujo visible."**

*[señalar slide 17]*

**"El stack completo de un agente en Stellar tiene estas capas: el LLM o la lógica que decide qué hacer, el SDK que traduce esas decisiones a operaciones de Stellar, Horizon como gateway a la red, y abajo el ledger con el consenso SCP y los contratos Soroban."**

**"Cada capa tiene sus herramientas, su documentación, y su comunidad. En la diapositiva final van los links para empezar."**

> 🎙️ **Tip:** Si tenés demo en vivo preparada, este es el momento de mostrarla — aunque sea testnet. Ver una transacción real en el explorador de Stellar (stellar.expert) genera mucho más impacto que cualquier slide.

---

## 🎃 SECCIÓN 5 — CIERRE (2 min)

### 🖥️ Slide 18 — "M3GAN ahora tiene wallet."
> **Subtítulo:** *"¿Qué vas a construir vos?"* 🎃
> **Fondo:** negro, con la escena de cierre (muñeca, luna y calabaza).
> **Links en pantalla:**
> - 🌐 `developers.stellar.org`
> - 🔎 `stellar.expert/explorer/testnet`
> - 🧪 `laboratory.stellar.org`
> **Pie:** *Stellar es una marca de Stellar Development Foundation. Presentación comunitaria independiente.*

---

### 📜 Libreto

**"Rápido resumen de lo que vimos:"**

**"Blockchain: lista enlazada distribuida y firmada criptográficamente. Consenso distribuido. Inmutabilidad por diseño."**

**"Stellar: consenso SCP en 3 a 5 segundos, fees de fracción de centavo, assets nativos, Soroban para contratos en Rust/WASM."**

**"Agentes en Stellar: wallet en tres líneas de código, micropagos programáticos, protocolo x402 para internet de máquinas, contratos como reglas auditables."**

*[pausa]*

**"La pregunta que me gustaría que se llevaran: con todo lo que escucharon hoy — de mis colegas y ahora de mí — ¿qué problema del mundo real les interesa resolver con un agente que tenga identidad económica en blockchain?"**

**"Remesas, pagos automatizados, servicios descentralizados, DeFi autónomo. El tooling está. La red está. La documentación está."**

*[señalar a M3GAN en el slide]*

**"M3GAN finalmente tiene billetera. Y es tuya para construirla."**

**"Gracias."** 🎃

> 🎙️ **Tip:** El cierre es breve e intencionalmente abierto. Con estudiantes de informática, la mejor llamada a la acción es *hacerlos pensar en un problema que quieren resolver*. El remate de M3GAN es el gancho de humor final que hace la charla memorable.

---

## 🖥️ GUÍA DE PRESENTACIÓN

### 🎨 Estética Visual

```
PALETA DEL DECK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Fondo:           #0F0F0F   Negro
  Amarillo:        #FDDA24   Acento Stellar / títulos clave
  Blanco:          #F6F7F8   Texto
  Lavanda:         #B7ACE8   Vestido, lápidas, luna
  Teal:            #00A7B5   Detalles y selección
  Azul:            #002E5D   Lazo y colinas
  Papel:           #D6D2C4   Tarjetas y tablas
Tipografías: Creepster (títulos) · Nunito (cuerpo) · IBM Plex Mono (código)
```

### 🎞️ Animaciones por sección

| Slide | Efecto recomendado |
|--|--|
| Apertura | Fade-in lento → ojos de M3GAN se iluminan |
| Slides 2–9 (interactivas) | Sub-slides paso a paso: bloques, red que propone y vota un bloque, campos, Merkle, dominó en rojo, consenso y quórums. Transiciones suaves, sin saltos |
| Tabla consenso | Columnas aparecen una a una, Stellar al final |
| Cuenta Stellar | Campos del objeto aparecen línea a línea |
| Diagrama x402 | Flechas que se mueven de izquierda a derecha, paso a paso |
| Stack completo | Capas apilándose de abajo hacia arriba |
| Cierre | Zoom suave a la cara de M3GAN + QR |

### 🛠️ Herramientas (las que usa este deck)

| Herramienta | Para qué |
|--|--|
| **Three.js + Anime.js** | Escena de papel recortado, personajes y transición de página |
| **`server.py`** | Sirve `dist/` y mantiene el estado compartido (slide, sub-paso, reloj) |
| **`/?notes`** | Libreto, reloj, salto de slides y panel de sub-slides en vivo |
| **`dist/acto2.html`** | Slides 2–9 interactivas, controladas por el servidor |

### ⏱️ Gestión del tiempo

| Sección | Máx. si vas bien | Recortar si vas tarde |
|--|--|--|
| Hook | 2 min | No recortar |
| Blockchain | 6 min | Saltar detalle Merkle |
| Stellar | 8 min | Simplificar SCP a 1 slide |
| Agentes+Stellar | 9 min | Omitir slide Soroban |
| Casos | 3 min | 1 solo caso en vez de 3 |
| Cierre | 2 min | No recortar |

### 🎤 Tips generales

- **Son informáticos** → puedes usar términos técnicos sin disculparte
- **Evita leer las slides** → son un apoyo visual, no tu guión
- **Snippets de código** → léelos en voz alta línea a línea, explica cada una
- **Demos en vivo > slides** → si puedes mostrar `stellar.expert` con una tx real, hazlo
- **Pausa después de x402** → es el concepto más nuevo y más impactante, deja que aterrice

---

### 🔗 Hilo conductor M3GAN (6 referencias)

| Momento | Uso |
|--|--|
| Apertura | *"Le damos billetera"* — gancho emocional |
| Problema de identidad | Imagen: M3GAN rechazada por el banco — ilustra el problema |
| x402 | Implícito: agente que compra servicios autónomamente |
| Soroban | *"Las reglas de M3GAN son código inmutable"* — confianza |
| Cierre | *"M3GAN finalmente tiene billetera"* — remate de humor |

---

### 📚 Recursos (compartir post-charla)

- [stellar.org/developers](https://stellar.org/developers) — punto de entrada
- [docs.stellar.org](https://docs.stellar.org) — documentación completa
- [x402.org](https://x402.org) — protocolo de micropagos HTTP
- [github.com/stellar/stellar-ai-toolkit](https://github.com/stellar/stellar-ai-toolkit) — SDK para agentes
- [stellar.expert](https://stellar.expert) — explorador de la red en vivo
- [laboratory.stellar.org](https://laboratory.stellar.org) — sandbox para construir transacciones

---

*Libreto v2.1 · sincronizado con el deck de 18 slides · Evento AI Agents + Blockchain Halloween 🎃 · Octubre 2026*
