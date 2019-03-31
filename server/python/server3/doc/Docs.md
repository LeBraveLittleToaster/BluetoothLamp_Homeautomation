# Modi

## General Packaging
x = [0,127] Integer <br />
| -- '#' -- | -- m -- | -- x0 -- | -- x1 -- | -- x2 -- | -- x3 -- | -- x4 -- | -- x5 -- |


### Modi definition

#### 1. Solid Color

x0-x5 * 2

| Key   | Value     |
|-------|-----------|
|m      | 0         |
|x0     | empty     |
|x1     | empty     |
|x2     | empty     |
|x3     | empty     |
|x4     | empty     |
|x5     | empty     |

#### 1. Solid Color

x0-x5 * 2

| Key   | Value     |
|-------|-----------|
|m      | 1         |
|x0     | hue     |
|x1     | saturation     |
|x2     | value     |
|x3     | empty     |
|x4     | empty     |
|x5     | empty     |


#### 2. Colorramp (singlecolor)

x0-x5 * 2

| Key   | Value     |
|-------|-----------|
|m      | 2         |
|x0     | hue     |
|x1     | saturation     |
|x2     | value     |
|x3     | color movement speed     |
|x4     | empty     |
|x5     | empty     |


#### 3. Colorramp (multicolor)

x0-x5 * 2

| Key   | Value     |
|-------|-----------|
|m      | 3         |
|x0     | empty     |
|x1     | empty     |
|x2     | empty     |
|x3     | color movement speed     |
|x4     | color shift speed     |
|x5     | empty     |


#### 4. Flicker (singlecolor)

x0-x5 * 2

| Key   | Value     |
|-------|-----------|
|m      | 4         |
|x0     | hue     |
|x1     | saturation     |
|x2     | value     |
|x3     | color spawn speed     |
|x4     | color spawn amount     |
|x5     | empty     |


#### 5. Flicker (multicolor)

x0-x5 * 2

| Key   | Value     |
|-------|-----------|
|m      | 5         |
|x0     | empty     |
|x1     | empty     |
|x2     | empty     |
|x3     | color spawn sped     |
|x4     | color spawn amount     |
|x5     | empty     |


#### 6. Pulse

x0-x5 * 2

| Key   | Value     |
|-------|-----------|
|m      | 6         |
|x0     | hue       |
|x1     | saturation|
|x2     | value     |
|x3     | pulsespeed|
|x4     | empty     |
|x5     | empty     |