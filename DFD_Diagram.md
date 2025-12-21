# Data Flow Diagram (DFD) - Comic Book Generator System

## DFD Level 0 (Context Diagram)

```
                    ┌─────────────────────────────────┐
                    │                                 │
    Story Text ────▶│   Comic Book Generator System  │────▶ Generated Comic
    Style Selection │                                 │      (PDF/PNG/JPG)
    Panel Config    │                                 │
                    └─────────────────────────────────┘
```

**External Entities:**
- User: Provides input and receives output
- Registered User: Logged-in user who can post creations

**Data Flows:**
- Input: Story Text, Style Selection, Panel Configuration, Login Credentials, Registration Data
- Output: Generated Comic (PDF/PNG/JPG formats), Gallery Posts, User Profile

---

## DFD Level 1 (System Overview)

```
┌─────────┐
│  User   │
└────┬────┘
     │
     │ Story Text, Style, Config
     ▼
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  ┌──────────────────┐                                       │
│  │  1.0 User       │                                       │
│  │  Interface      │                                       │
│  │  Module         │                                       │
│  └──────┬──────────┘                                       │
│         │                                                   │
│         │ Processed Input                                   │
│         ▼                                                   │
│  ┌──────────────────┐                                       │
│  │  2.0 Text       │                                       │
│  │  Processing &   │                                       │
│  │  Prompt         │                                       │
│  │  Generation     │                                       │
│  └──────┬──────────┘                                       │
│         │                                                   │
│         │ Optimized Prompts                                 │
│         ▼                                                   │
│  ┌──────────────────┐                                       │
│  │  3.0 Stable      │                                       │
│  │  Diffusion       │                                       │
│  │  Image           │                                       │
│  │  Generation      │                                       │
│  └──────┬──────────┘                                       │
│         │                                                   │
│         │ Generated Images                                   │
│         ▼                                                   │
│  ┌──────────────────┐                                       │
│  │  4.0 Panel        │                                       │
│  │  Layout &         │                                       │
│  │  Dialogue         │                                       │
│  └──────┬──────────┘                                       │
│         │                                                   │
│         │ Formatted Panels                                  │
│         ▼                                                   │
│  ┌──────────────────┐                                       │
│  │  5.0 Rendering   │                                       │
│  │  & Export        │                                       │
│  └──────┬──────────┘                                       │
│         │                                                   │
│         │ Final Comic                                       │
│         ▼                                                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
     │
     │ Generated Comic (PDF/PNG/JPG)
     ▼
┌─────────┐
│  User   │
└─────────┘
```

**Processes:**
1. 1.0 User Interface Module
2. 2.0 Text Processing & Prompt Generation Module
3. 3.0 Stable Diffusion Image Generation Module
4. 4.0 Comic Panel Layout & Dialogue Module
5. 5.0 Rendering & Export Module

**Data Stores:**
- D1: User Projects Database
- D2: Generated Images Storage
- D3: Character Reference Library
- D4: Project Templates
- D5: User Accounts Database
- D6: User Creations Gallery
- D7: Comments and Likes Database

---

## DFD Level 2 (Detailed Process Flows)

### Process 1.0: User Interface Module

```
┌─────────┐
│  User   │
└────┬────┘
     │
     │ Story Input, Style Selection, Panel Config
     ▼
┌──────────────────────────────────────────────┐
│  1.0 User Interface Module                   │
│                                              │
│  ┌──────────────┐  ┌──────────────┐         │
│  │ 1.1 Input   │  │ 1.2 Style    │         │
│  │ Validation  │  │ Selection    │         │
│  └──────┬───────┘  └──────┬───────┘         │
│         │                 │                  │
│         └────────┬────────┘                  │
│                  │                            │
│                  │ Validated Input            │
│                  ▼                            │
│         ┌──────────────────┐                  │
│         │ 1.3 Preview      │                  │
│         │ Generator        │                  │
│         └──────────────────┘                  │
│                                              │
└──────────────────┬───────────────────────────┘
                   │
                   │ Processed User Input
                   ▼
            ┌──────────────┐
            │   Process    │
            │     2.0      │
            └──────────────┘
```

**Data Flows:**
- Input: Story Text, Style Selection, Panel Configuration
- Output: Validated and Processed Input
- To D1: Save Project Data

---

### Process 2.0: Text Processing & Prompt Generation

```
                   ┌──────────────┐
                   │   Process    │
                   │     1.0      │
                   └──────┬───────┘
                          │
                          │ User Input Text
                          ▼
┌─────────────────────────────────────────────────────┐
│  2.0 Text Processing & Prompt Generation            │
│                                                      │
│  ┌──────────────┐  ┌──────────────┐                │
│  │ 2.1 Scene   │  │ 2.2 Entity   │                │
│  │ Segmentation│  │ Extraction   │                │
│  └──────┬───────┘  └──────┬───────┘                │
│         │                 │                         │
│         └────────┬────────┘                         │
│                  │                                  │
│                  │ Extracted Data                   │
│                  ▼                                  │
│         ┌──────────────────┐                        │
│         │ 2.3 Prompt       │                        │
│         │ Optimization     │                        │
│         └──────┬───────────┘                        │
│                │                                     │
│                │ Character Reference                 │
│                ▼                                     │
│         ┌──────────────────┐                        │
│         │ 2.4 Consistency │                        │
│         │ Checker         │                        │
│         └──────────────────┘                        │
│                                                      │
└──────────────────┬──────────────────────────────────┘
                   │
                   │ Optimized Prompts
                   ▼
            ┌──────────────┐
            │   Process    │
            │     3.0      │
            └──────────────┘
                   │
                   │ Character Data
                   ▼
            ┌──────────────┐
            │  D3: Char    │
            │  Reference   │
            │  Library     │
            └──────────────┘
```

**Data Flows:**
- Input: User Input Text
- Output: Optimized Prompts for Image Generation
- To D3: Character Reference Data
- From D3: Character Consistency Data

---

### Process 3.0: Stable Diffusion Image Generation

```
                   ┌──────────────┐
                   │   Process    │
                   │     2.0      │
                   └──────┬───────┘
                          │
                          │ Optimized Prompts
                          ▼
┌─────────────────────────────────────────────────────┐
│  3.0 Stable Diffusion Image Generation               │
│                                                      │
│  ┌──────────────┐  ┌──────────────┐                │
│  │ 3.1 Prompt   │  │ 3.2 Style    │                │
│  │ Processing  │  │ Application  │                │
│  └──────┬───────┘  └──────┬───────┘                │
│         │                 │                         │
│         └────────┬────────┘                         │
│                  │                                  │
│                  │ Style-Enhanced Prompts          │
│                  ▼                                  │
│         ┌──────────────────┐                        │
│         │ 3.3 Stable      │                        │
│         │ Diffusion API   │                        │
│         │ Call            │                        │
│         └──────┬───────────┘                        │
│                │                                     │
│                │ Generated Images                   │
│                ▼                                     │
│         ┌──────────────────┐                        │
│         │ 3.4 Image       │                        │
│         │ Post-Processing │                        │
│         └──────────────────┘                        │
│                                                      │
└──────────────────┬──────────────────────────────────┘
                   │
                   │ Generated Images
                   ▼
            ┌──────────────┐
            │   Process    │
            │     4.0      │
            └──────────────┘
                   │
                   │ Images
                   ▼
            ┌──────────────┐
            │  D2: Image   │
            │  Storage     │
            └──────────────┘
```

**Data Flows:**
- Input: Optimized Prompts, Style Parameters
- Output: Generated Comic Images
- To D2: Store Generated Images
- External: Stable Diffusion API

---

### Process 4.0: Comic Panel Layout & Dialogue

```
                   ┌──────────────┐
                   │   Process    │
                   │     3.0      │
                   └──────┬───────┘
                          │
                          │ Generated Images
                          ▼
┌─────────────────────────────────────────────────────┐
│  4.0 Comic Panel Layout & Dialogue                   │
│                                                      │
│  ┌──────────────┐  ┌──────────────┐                │
│  │ 4.1 Panel   │  │ 4.2 Dialogue│                │
│  │ Layout      │  │ Extraction   │                │
│  │ Engine      │  │              │                │
│  └──────┬───────┘  └──────┬───────┘                │
│         │                 │                         │
│         └────────┬────────┘                         │
│                  │                                  │
│                  │ Layout Data                      │
│                  ▼                                  │
│         ┌──────────────────┐                        │
│         │ 4.3 Speech      │                        │
│         │ Bubble          │                        │
│         │ Placement       │                        │
│         └──────┬───────────┘                        │
│                │                                     │
│                │ Formatted Panels                   │
│                ▼                                     │
│         ┌──────────────────┐                        │
│         │ 4.4 Sound       │                        │
│         │ Effects &       │                        │
│         │ Final Layout    │                        │
│         └──────────────────┘                        │
│                                                      │
└──────────────────┬──────────────────────────────────┘
                   │
                   │ Formatted Comic Panels
                   ▼
            ┌──────────────┐
            │   Process    │
            │     5.0      │
            └──────────────┘
```

**Data Flows:**
- Input: Generated Images, Dialogue Text
- Output: Formatted Comic Panels with Dialogue

---

### Process 5.0: Rendering & Export

```
                   ┌──────────────┐
                   │   Process    │
                   │     4.0      │
                   └──────┬───────┘
                          │
                          │ Formatted Panels
                          ▼
┌─────────────────────────────────────────────────────┐
│  5.0 Rendering & Export                             │
│                                                      │
│  ┌──────────────┐  ┌──────────────┐                │
│  │ 5.1 High-Res │  │ 5.2 Format   │                │
│  │ Rendering    │  │ Conversion  │                │
│  └──────┬───────┘  └──────┬───────┘                │
│         │                 │                         │
│         └────────┬────────┘                         │
│                  │                                  │
│                  │ Rendered Pages                  │
│                  ▼                                  │
│         ┌──────────────────┐                        │
│         │ 5.3 PDF/Image   │                        │
│         │ Generation      │                        │
│         └──────┬───────────┘                        │
│                │                                     │
│                │ Final Comic                        │
│                ▼                                     │
│         ┌──────────────────┐                        │
│         │ 5.4 Quality      │                        │
│         │ Control &       │                        │
│         │ Export           │                        │
│         └──────────────────┘                        │
│                                                      │
└──────────────────┬──────────────────────────────────┘
                   │
                   │ Final Comic (PDF/PNG/JPG)
                   ▼
            ┌──────────────┐
            │  D2: Final   │
            │  Output      │
            │  Storage     │
            └──────────────┘
                   │
                   │ Download Link
                   ▼
            ┌──────────────┐
            │     User     │
            └──────────────┘
```

**Data Flows:**
- Input: Formatted Comic Panels
- Output: Final Comic (PDF/PNG/JPG)
- To D2: Store Final Output
- To User: Download Link

---

### Process 6.0: User Authentication & Registration

```
┌─────────┐
│  User   │
└────┬────┘
     │
     │ Registration/Login Data
     ▼
┌─────────────────────────────────────────────────────┐
│  6.0 User Authentication & Registration            │
│                                                      │
│  ┌──────────────┐  ┌──────────────┐                │
│  │ 6.1 User     │  │ 6.2 Login    │                │
│  │ Registration │  │ Authentication│                │
│  └──────┬───────┘  └──────┬───────┘                │
│         │                 │                         │
│         │ User Data       │ Login Credentials        │
│         ▼                 ▼                         │
│  ┌──────────────────┐  ┌──────────────────┐       │
│  │ 6.3 Email        │  │ 6.4 Session      │       │
│  │ Verification     │  │ Management       │       │
│  └──────────────────┘  └──────────────────┘       │
│                                                      │
└──────────────────┬──────────────────────────────────┘
                   │
                   │ User Account Data
                   ▼
            ┌──────────────┐
            │  D5: User    │
            │  Accounts    │
            │  Database    │
            └──────────────┘
                   │
                   │ Authentication Token
                   ▼
            ┌──────────────┐
            │     User     │
            │  (Logged In) │
            └──────────────┘
```

**Data Flows:**
- Input: Registration Data (email, password, username), Login Credentials
- Output: Authentication Token, User Profile
- To D5: Store User Account Data
- From D5: Retrieve User Data for Login

---

### Process 7.0: User Creations Gallery

```
┌──────────────┐
│ Logged-in    │
│ User         │
└──────┬───────┘
       │
       │ Post Creation Request
       ▼
┌─────────────────────────────────────────────────────┐
│  7.0 User Creations Gallery                          │
│                                                      │
│  ┌──────────────┐  ┌──────────────┐                │
│  │ 7.1 Creation │  │ 7.2 Gallery │                │
│  │ Posting      │  │ Browsing    │                │
│  └──────┬───────┘  └──────┬───────┘                │
│         │                 │                         │
│         │ Posted Creation │ Browse Request          │
│         ▼                 ▼                         │
│  ┌──────────────────┐  ┌──────────────────┐       │
│  │ 7.3 Content     │  │ 7.4 User        │       │
│  │ Moderation      │  │ Interactions     │       │
│  └──────┬──────────┘  └──────┬───────────┘       │
│         │                     │                     │
│         │ Approved Creation   │ Like/Comment Data   │
│         ▼                     ▼                     │
│  ┌──────────────────┐  ┌──────────────────┐     │
│  │ 7.5 Gallery      │  │ 7.6 Social      │     │
│  │ Management       │  │ Features        │     │
│  └──────────────────┘  └──────────────────┘     │
│                                                      │
└──────────────────┬──────────────────────────────────┘
                   │
                   │ Gallery Data
                   ▼
            ┌──────────────┐
            │  D6: User    │
            │  Creations   │
            │  Gallery     │
            └──────────────┘
                   │
                   │ Interaction Data
                   ▼
            ┌──────────────┐
            │  D7: Comments│
            │  & Likes     │
            │  Database    │
            └──────────────┘
                   │
                   │ Gallery Feed
                   ▼
            ┌──────────────┐
            │     Users    │
            │  (All Users) │
            └──────────────┘
```

**Data Flows:**
- Input: Posted Creation (comic, title, description, tags), Browse/Filter Requests
- Output: Gallery Feed, Creation Details, User Interactions
- To D6: Store Posted Creations
- To D7: Store Comments, Likes, Follows
- From D5: User Profile Data
- From D2: Comic Images for Display

---

## Data Dictionary

### Data Stores

**D1: User Projects Database**
- Project ID
- User ID
- Story Text
- Style Selection
- Panel Configuration
- Creation Date
- Last Modified

**D2: Generated Images Storage**
- Image ID
- Project ID
- Image File Path
- Generation Timestamp
- Image Metadata

**D3: Character Reference Library**
- Character ID
- Character Attributes
- Appearance Description
- Reference Images
- Consistency Parameters

**D4: Project Templates**
- Template ID
- Template Name
- Default Settings
- Layout Presets

**D5: User Accounts Database**
- User ID
- Username
- Email Address
- Password Hash
- Profile Information
- Account Status
- Registration Date
- Last Login

**D6: User Creations Gallery**
- Creation ID
- User ID (Creator)
- Comic File Reference
- Title
- Description
- Tags
- Category
- Visibility Setting
- Post Date
- View Count
- Like Count

**D7: Comments and Likes Database**
- Interaction ID
- Creation ID
- User ID
- Interaction Type (Like, Comment, Follow)
- Comment Text (if applicable)
- Timestamp

### Data Flows

**Story Text**
- Type: Text String
- Description: User-provided narrative or scene descriptions
- Source: User
- Destination: Process 1.0

**Style Selection**
- Type: Enum (Manga, Cartoon, Western)
- Description: Selected comic art style
- Source: User
- Destination: Process 1.0

**Optimized Prompts**
- Type: Structured Text
- Description: AI-optimized prompts for image generation
- Source: Process 2.0
- Destination: Process 3.0

**Generated Images**
- Type: Image Files (PNG/JPEG)
- Description: Comic-style images generated by Stable Diffusion
- Source: Process 3.0
- Destination: Process 4.0, D2

**Formatted Panels**
- Type: Image Files with Overlays
- Description: Comic panels with dialogue, borders, and effects
- Source: Process 4.0
- Destination: Process 5.0

**Final Comic**
- Type: PDF/PNG/JPEG Files
- Description: Complete comic book ready for distribution
- Source: Process 5.0
- Destination: User, D2

**User Registration Data**
- Type: Structured Data
- Description: User account information for registration
- Source: User
- Destination: Process 6.0, D5

**Login Credentials**
- Type: Authentication Data
- Description: Email and password for user authentication
- Source: User
- Destination: Process 6.0

**Authentication Token**
- Type: JWT Token
- Description: Session token for authenticated users
- Source: Process 6.0
- Destination: User, Other Processes

**Posted Creation**
- Type: Structured Data with File Reference
- Description: User-posted comic with metadata
- Source: Logged-in User
- Destination: Process 7.0, D6

**Gallery Feed**
- Type: Collection of Creations
- Description: List of user-posted comics for browsing
- Source: Process 7.0, D6
- Destination: All Users

---

## DFD Summary

**Level 0:** Shows the system as a single process interacting with the user

**Level 1:** Breaks down the system into 7 main processes showing data flow between modules (5 core + 2 user management)

**Level 2:** Provides detailed view of each process with sub-processes and internal data flows

**Key Data Stores:**
- D1: User Projects Database
- D2: Generated Images Storage
- D3: Character Reference Library
- D4: Project Templates
- D5: User Accounts Database
- D6: User Creations Gallery
- D7: Comments and Likes Database

**External Entities:**
- User: Input provider and output receiver (anonymous)
- Registered User: Logged-in user who can post creations
- Stable Diffusion API: External service for image generation

