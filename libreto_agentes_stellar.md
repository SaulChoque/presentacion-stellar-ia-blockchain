# 🎃 Libreto v2: Agentes en la Red Stellar
### *"Blockchain sin misterio: redes, transacciones y ecosistema"*
**Evento:** AI Agents + Blockchain Halloween · [Luma](https://luma.com/742fo5f8)
**Charla #03 · Duración: 25–30 min · Público: Estudiantes de Informática**

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
> **Fondo:** Negro total. Aparece lentamente el texto:
> *"Ya saben qué es un agente. Ya saben lo que puede hacer."*
> Pausa → Ojos de M3GAN se encienden.
> **Texto nuevo:** *"Esta noche le damos billetera."* 🎃

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

### 🖥️ Slide 2
> **Título:** "Blockchain: lo que ya intuyes + lo que falta"
> **Visual:** Diagrama de una linked list → evoluciona a una cadena de bloques
> Texto: *"Es una lista enlazada… pero distribuida, firmada criptográficamente e inmutable."*

---

### 🖥️ Slide 3
> **Título:** "Anatomía de un bloque"
> **Visual:** Bloque con sus campos anotados (estilo diagrama técnico):
> ```
> ┌─────────────────────────────────┐
> │  Block Header                   │
> │  ├─ prev_hash: 0xA3F2...        │
> │  ├─ timestamp: 1730150400       │
> │  ├─ merkle_root: 0x9C1D...      │
> │  └─ nonce / validator_sig       │
> ├─────────────────────────────────┤
> │  Transactions []                │
> │  ├─ tx_0: Alice → Bob 10 XLM   │
> │  ├─ tx_1: Bob → Carol 5 XLM    │
> │  └─ ...                         │
> └─────────────────────────────────┘
> ```

---

### 🖥️ Slide 4
> **Título:** "¿Por qué es inmutable?"
> **Visual:** Diagrama de 3 bloques encadenados. Se intenta modificar el bloque 2:
> - El hash del bloque 2 cambia → invalida el bloque 3 → y todos los siguientes
> - Animación: efecto dominó de bloques "rompiéndose" en rojo
> **Texto:** *"Cambiar un bloque rompe la cadena. La red lo detecta y lo rechaza."*

---

### 🖥️ Slide 5
> **Título:** "Consenso: ¿quién decide qué es válido?"
> **Visual:** Tabla comparativa — solo los mecanismos relevantes
>
> | Mecanismo | Quién valida | Costo energético | Velocidad |
> |--|--|--|--|
> | **PoW** (Bitcoin) | Mineros (CPU/GPU) | 🔥🔥🔥 Alto | ~10 min |
> | **PoS** (Ethereum) | Validadores con stake | 🔥 Medio | ~15 seg |
> | **SCP** (Stellar) | Quórum de nodos de confianza | ✅ Mínimo | **3–5 seg** |

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

**"Para atacar exitosamente la red, necesitarías controlar más del 50% de los nodos. En redes grandes, eso es prácticamente imposible."**

*[señalar slide 5]*

**"Ahora, el mecanismo de consenso es donde las blockchains se diferencian. Bitcoin usa Proof of Work — competencia de cómputo brutal, energéticamente costosa. Ethereum usa Proof of Stake — mejor, pero sigue siendo lento para micropagos."**

**"Stellar usa algo diferente: el Stellar Consensus Protocol, o SCP. En vez de competir, los nodos definen 'quórums de confianza' — conjuntos de nodos en los que confían. El consenso emerge de esos quórums superpuestos. El resultado: finalidad en 3 a 5 segundos, con costo computacional mínimo."**

**"Ya entraremos al detalle de SCP. Primero entendamos por qué Stellar en particular."**

> 🎙️ **Tip:** Puedes preguntar rápido: *"¿Cuántos ya habían escuchado de Merkle trees?"* — conecta con lo que ya saben. No te extiendas en la teoría de consenso todavía, solo siembra la curiosidad para el siguiente bloque.

---

## ⭐ SECCIÓN 2 — Stellar: arquitectura y por qué importa (8 min)

### 🖥️ Slide 6
> **Título:** "Stellar Consensus Protocol (SCP)"
> **Visual:** Diagrama de quórum:
> ```
>   Nodo A ←──── Nodo B ←──── Nodo C
>     │             │             │
>     └─────────────┼─────────────┘
>               Quórum
>
>  Si A, B y C están de acuerdo → bloque confirmado ✅
>  Si C discrepa → vuelven a votar ♻️
> ```
> **Nota:** *"No hay un líder. No hay mineros. Solo acuerdo matemático entre nodos de confianza."*

---

### 🖥️ Slide 7
> **Título:** "Cuentas y Assets en Stellar"
> **Visual:** Diagrama de cuenta Stellar con sus campos
> ```
> Account {
>   public_key:  GABC...XYZ      ← dirección pública (Ed25519)
>   secret_key:  SABC...XYZ      ← firma transacciones (NUNCA comparte)
>   balances: [
>     { asset: XLM,  amount: 100.5 },
>     { asset: USDC, amount: 50.0  },
>     { asset: "MY_TOKEN:GISSUER", amount: 200 }
>   ]
>   sequence_number: 12345678    ← evita replay attacks
> }
> ```

---

### 🖥️ Slide 8
> **Título:** "Operaciones: los verbos de Stellar"
> **Visual:** Lista de operaciones más comunes con íconos
>
> | Operación | Qué hace |
> |--|--|
> | `Payment` | Envía XLM o cualquier asset |
> | `ChangeTrust` | Habilita recibir un asset |
> | `ManageSellOffer` | Crea orden en el DEX |
> | `InvokeContractFunction` | Llama a un smart contract (Soroban) |
> | `SetOptions` | Configura multisig, umbrales |
>
> **Nota:** *Varias operaciones pueden agruparse en una sola transacción. Atómicas.*

---

### 🖥️ Slide 9
> **Título:** "Soroban: Smart contracts en Stellar"
> **Visual:** Stack visual:
> ```
> ┌──────────────────────────────┐
> │   Tu contrato  (.wasm)       │  ← Escrito en Rust
> ├──────────────────────────────┤
> │   WebAssembly Runtime        │  ← Sandbox seguro
> ├──────────────────────────────┤
> │   Stellar Ledger             │  ← Estado persistente
> └──────────────────────────────┘
> ```
> **Texto:** *"Contratos en Rust → compilados a WASM → ejecutados on-chain. Deterministas, auditables."*

---

### 🖥️ Slide 10
> **Título:** "¿Por qué Stellar y no otra blockchain?"
> **Visual:** Tarjetas de ventajas con números reales
>
> ```
>  ⚡ Finalidad:   3–5 segundos
>  💸 Fee:         0.00001 XLM (~$0.000003 USD)
>  🌐 Throughput:  ~1,000 tx/seg (en producción)
>  💵 USDC nativo: Sin bridges, sin wrapping
>  🏦 Adopción:    MoneyGram, Circle, Banco Central de Ucrania
> ```

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

### 🖥️ Slide 11
> **Título:** "El problema: los agentes no tienen identidad financiera"
> **Visual:** M3GAN intentando pagar con tarjeta → rechazada ❌
> **Texto:** *"No tienen DNI. No pueden abrir cuenta bancaria. El sistema financiero tradicional no fue diseñado para software autónomo."*

---

### 🖥️ Slide 12
> **Título:** "Solución: crear una wallet on-chain en segundos"
> **Visual:** Snippet de código animado (aparece línea a línea)
> ```python
> from stellar_sdk import Keypair, Server, TransactionBuilder, Network
>
> # 1. Generar identidad del agente
> agent_keypair = Keypair.random()
> print(f"Agent address: {agent_keypair.public_key}")
> # → GABC...XYZ
>
> # 2. Fondear la cuenta (mínimo 1 XLM de reserva)
> #    En testnet: friendbot lo hace gratis
> #    En mainnet: otro agente o el usuario lo fondea
>
> # 3. El agente ya puede enviar pagos
> server = Server("https://horizon-testnet.stellar.org")
> ```
> **Nota:** *"3 líneas para dar identidad financiera a cualquier proceso de software."*

---

### 🖥️ Slide 13
> **Título:** "Flujo de un agente haciendo un micropago"
> **Visual:** Diagrama de secuencia animado (aparece paso a paso)
> ```
> Agente                    Horizon API               Stellar Network
>   │                           │                           │
>   │── build_transaction() ───►│                           │
>   │   (Payment op, 0.001 USDC)│                           │
>   │◄── unsigned_tx ───────────│                           │
>   │                           │                           │
>   │── sign(secret_key) ───────────────────────────────────│
>   │── submit_transaction() ──►│                           │
>   │                           │── broadcast ─────────────►│
>   │                           │                           │── validate
>   │                           │                           │── consensus
>   │◄── 200 OK (3-5 seg) ──────│◄── confirmed ─────────────│
>   │                           │                           │
> ```

---

### 🖥️ Slide 14
> **Título:** "El protocolo x402: internet de máquinas"
> **Visual:** Diagrama de flujo HTTP animado
> ```
>   Agente                                   API Server
>     │                                           │
>     │──── GET /premium-data ───────────────────►│
>     │                                           │
>     │◄─── 402 Payment Required ─────────────────│
>     │     { amount: "0.001", asset: "USDC",     │
>     │       address: "GSERVER...",              │
>     │       network: "stellar:mainnet" }        │
>     │                                           │
>     │──── [paga 0.001 USDC en Stellar] ─────────┤
>     │──── GET /premium-data                     │
>     │     Authorization: x402 <tx_hash> ───────►│
>     │                                           │── verifica pago on-chain
>     │◄─── 200 OK + data ────────────────────────│
> ```
> **Nota:** *"El código HTTP 402 existió desde 1991. Esperó 30 años para ser usado por máquinas."*

---

### 🖥️ Slide 15
> **Título:** "Contratos como reglas inmutables del agente"
> **Visual:** Dos columnas
>
> **Sin Soroban:**
> ```
> Usuario confía en que
> el agente hace lo correcto.
> Caja negra. Sin auditoría.
> ```
>
> **Con Soroban:**
> ```rust
> // El agente SOLO puede gastar
> // hasta este límite por día
> #[contract]
> pub fn transfer(env: Env, to: Address, amount: i128) {
>     let daily_limit: i128 = 100_000_000; // 10 USDC
>     let spent_today = env.storage().get_spent_today();
>     assert!(spent_today + amount <= daily_limit);
>     // ... ejecuta el pago
> }
> ```
> **Texto:** *"Las reglas del agente son código on-chain. Verificables. Inmutables. Sin excepciones."*

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

**"El agente lee eso, ejecuta el pago en Stellar, incluye el hash de la transacción en el header de la siguiente request, y el servidor verifica on-chain que el pago llegó. Si llegó, entrega el recurso."**

**"Todo esto ocurre en segundos, sin humanos, sin contratos firmados, sin subscripciones mensuales. Las máquinas se están pagando entre sí en tiempo real."**

**"El código 402 existió en la especificación HTTP desde 1991. Tim Berners-Lee lo incluyó pensando que eventualmente se usaría para micropagos en la web. Tardó 30 años en materializarse, y la herramienta que lo hizo posible fue Stellar."**

*[señalar slide 15]*

**"Y hay algo muy relevante para la confianza en sistemas autónomos: Soroban permite que las reglas bajo las cuales opera el agente sean código on-chain."**

**"Si le dices al usuario 'mi agente nunca va a gastar más de 10 USDC al día', eso puede estar codificado en un contrato inmutable en Stellar. No es una promesa. Es código que la red ejecuta."**

**"Para sistemas de producción donde un agente maneja fondos reales de usuarios, esto es la diferencia entre 'confíenme' y 'verifíquenlo ustedes mismos'. La auditoría es pública, permanente y sin intermediarios."**

> 🎙️ **Tip:** El slide de x402 es el más denso visualmente. Pasa por él despacio — es el momento más técnico y más impactante. Si ves que el tiempo se acaba, puedes recortar el slide 15 de Soroban a solo 1 minuto de mención rápida.

---

## 🌍 SECCIÓN 4 — Demo / Casos Reales (3 min)

### 🖥️ Slide 16
> **Título:** "Casos reales operando hoy"
> **Visual:** Tres tarjetas

**🏦 Remesas sin intermediarios**
> MoneyGram + Stellar: personas en América Latina y África reciben remesas en segundos, sin cuenta bancaria. El agente de conversión opera automáticamente en el DEX de Stellar.

**🤖 Trading autónomo 24/7**
> Bots operando en el Stellar DEX, ejecutando arbitraje y market-making. Micropagos de fees por cada operación — económicamente viable solo por los costos de Stellar.

**🔐 KYC descentralizado con agentes**
> Agentes de verificación de identidad usando el protocolo SEP-30 de Stellar. Verifican sin guardar datos en servidores centrales — los datos viven en la blockchain, controlados por el usuario.

---

### 🖥️ Slide 17
> **Título:** "El stack completo de un agente en Stellar"
> **Visual:** Diagrama de capas (de arriba a abajo)
> ```
> ┌─────────────────────────────────────────┐
> │   LLM / Lógica del Agente               │  ← Claude, GPT, Gemini...
> ├─────────────────────────────────────────┤
> │   Stellar AI Toolkit / SDK              │  ← stellar-sdk, x402-client
> ├─────────────────────────────────────────┤
> │   Horizon API                           │  ← Gateway a la red
> ├─────────────────────────────────────────┤
> │   Stellar Network (SCP)                 │  ← Consenso, ledger
> ├─────────────────────────────────────────┤
> │   Soroban Contracts                     │  ← Reglas inmutables
> └─────────────────────────────────────────┘
> ```

---

### 📜 Libreto

**"Tres ejemplos concretos de hoy, no del futuro."**

*[tarjeta por tarjeta]*

**"MoneyGram usa Stellar en producción para remesas. El proceso involucra agentes de conversión que operan automáticamente en el DEX de Stellar — convirtiendo USD a XLM, ejecutando el pago, convirtiendo del otro lado. El usuario solo ve que su familiar recibió dinero en minutos."**

**"En el DEX de Stellar hay bots de trading operando continuamente. Market makers, arbitrajistas. En Ethereum el gas haría eso prohibitivo. En Stellar los fees son tan bajos que el modelo funciona con márgenes de décimas de centavo."**

**"Y hay proyectos usando el protocolo SEP-30 de Stellar para verificación de identidad descentralizada. Un agente puede verificar que eres quien dices ser sin que tus datos toquen un servidor central hackeable."**

*[señalar slide 17]*

**"El stack completo de un agente en Stellar tiene estas capas: el LLM o la lógica que decide qué hacer, el SDK que traduce esas decisiones a operaciones de Stellar, Horizon como gateway a la red, y abajo el ledger con el consenso SCP y los contratos Soroban."**

**"Cada capa tiene sus herramientas, su documentación, y su comunidad. En la diapositiva final van los links para empezar."**

> 🎙️ **Tip:** Si tenés demo en vivo preparada, este es el momento de mostrarla — aunque sea testnet. Ver una transacción real en el explorador de Stellar (stellar.expert) genera mucho más impacto que cualquier slide.

---

## 🎃 SECCIÓN 5 — CIERRE (2 min)

### 🖥️ Slide 18
> **Fondo:** Negro. M3GAN con su cara iluminada, pero ahora tiene debajo un QR de Stellar docs.
> **Texto:**
> *"M3GAN ahora tiene wallet."*
> *"¿Qué vas a construir vos?"* 🎃
>
> **Links:**
> - 🌐 `stellar.org/developers`
> - 📖 `docs.stellar.org`
> - ⚡ `x402.org`
> - 🧰 `github.com/stellar/stellar-ai-toolkit`

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
PALETA DE COLORES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Fondo:           #0A0A0A   Negro profundo
  Acento Stellar:  #7B61FF   Violeta
  Halloween:       #FF6B00   Naranja calabaza
  Código:          #00E8D0   Cyan (ojos de M3GAN)
  Texto:           #FFFFFF
  Texto sec.:      #AAAAAA
```

### 🎞️ Animaciones por sección

| Slide | Efecto recomendado |
|--|--|
| Apertura | Fade-in lento → ojos de M3GAN se iluminan |
| Bloques (Sección 1) | Diagrama construyéndose bloque a bloque |
| Tabla consenso | Columnas aparecen una a una, Stellar al final |
| Cuenta Stellar | Campos del objeto aparecen línea a línea |
| Diagrama x402 | Flechas que se mueven de izquierda a derecha, paso a paso |
| Stack completo | Capas apilándose de abajo hacia arriba |
| Cierre | Zoom suave a la cara de M3GAN + QR |

### 🛠️ Herramientas sugeridas

| Herramienta | Por qué |
|--|--|
| **Pitch.com** | Animaciones fluidas, tema oscuro, colaborativo |
| **Canva** | Templates oscuros, rápido de armar |
| **Gamma.app** | Genera slides desde este libreto con IA |
| **Excalidraw** | Para los diagramas técnicos (exporta como imagen) |

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

*Libreto v2 · Evento AI Agents + Blockchain Halloween 🎃 · Octubre 2026*
