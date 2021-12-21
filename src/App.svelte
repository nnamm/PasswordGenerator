<script>
  const initPasswd = '--------';
  let passwdLength = 0;
  let digitsLength = 0;
  let symbolsLength = 0;
  let inputText = '';
  let isIncludeToday = false;
  let generetedPasswd = initPasswd;
  export let name;

  const generatePasswd = async () => {
    // IP address is Ubuntu on Parallels
    const endpoint = 'http://10.211.55.4:8000/gen_passwd/';
    const params = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        passwd_length: passwdLength,
        digits_length: digitsLength,
        symbols_length: symbolsLength,
        input_text: inputText.replace(/\s+/g, ''),
        is_include_today: isIncludeToday,
      }),
    };
    console.log(params);

    const response = await fetch(endpoint, params);
    const data = await response.json();
    if (data.Passwd === 'None') {
      generetedPasswd = initPasswd;
    } else {
      generetedPasswd = data.Passwd;
    }
  };
</script>

<main>
  <h1>Hello {name}</h1>
  <div class="input-area">
    <!-- Input area / range -->
    <table class="options">
      <tbody>
        <tr>
          <td class="left">
            <!-- svelte-ignore a11y-label-has-associated-control -->
            <label>Length</label>
          </td>
          <td class="center">
            <input type="range" bind:value={passwdLength} min="0" max="128" on:change={generatePasswd} />
          </td>
          <td class="right">{passwdLength}</td>
        </tr>
        <tr>
          <td class="left">
            <!-- svelte-ignore a11y-label-has-associated-control -->
            {#if inputText.length > 0}
              <label class="disableFont">Digits</label>
            {:else}
              <label>Digits</label>
            {/if}
          </td>
          <td class="center">
            {#if inputText.length > 0}
              <input
                type="range"
                bind:value={digitsLength}
                min="0"
                max="20"
                on:change={generatePasswd}
                disabled="disabled"
              />
            {:else}
              <input type="range" bind:value={digitsLength} min="0" max="20" on:change={generatePasswd} />
            {/if}
          </td>
          <td class="right">{digitsLength}</td>
        </tr>
        <tr>
          <td class="left">
            <!-- svelte-ignore a11y-label-has-associated-control -->
            {#if inputText.length > 0}
              <label class="disableFont">Symbols</label>
            {:else}
              <label>Symbols</label>
            {/if}
          </td>
          <td class="center">
            {#if inputText.length > 0}
              <input
                type="range"
                bind:value={symbolsLength}
                min="0"
                max="20"
                on:change={generatePasswd}
                disabled="disabled"
              />
            {:else}
              <input type="range" bind:value={symbolsLength} min="0" max="20" on:change={generatePasswd} />
            {/if}
          </td>
          <td class="right">{symbolsLength}</td>
        </tr>
      </tbody>
    </table>

    <!-- Input area / text -->
    <label class="input-text">
      <p>Text want to use for password</p>
      <textarea maxlength="128" bind:value={inputText} on:input={generatePasswd} />
    </label>
    <!-- svelte-ignore a11y-label-has-associated-control -->
    <label class="today">
      {#if inputText.length > 0}
        <input type="checkbox" bind:checked={isIncludeToday} on:change={generatePasswd} />
        Include today's date (mmdd) ?
      {:else}
        <input type="checkbox" bind:checked={isIncludeToday} on:change={generatePasswd} disabled="disabled" />
        <span class="disableFont">Include today's date (mmdd) ?</span>
      {/if}
    </label>
  </div>

  <!-- Generated password area -->
  <div>
    <p class="passwd-title">Password</p>
    <p class="passwd">{generetedPasswd}</p>
  </div>
</main>

<style>
  main {
    text-align: center;
    min-width: 360px;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4rem;
    font-weight: 100;
  }

  .input-area {
    margin: 0 0.5rem 3rem 0.5rem;
  }

  .options {
    margin: auto;
  }

  .options .left {
    padding: 0.2rem;
    width: 5rem;
    text-align: right;
  }

  .options .center {
    padding: 0.5rem 1.2rem;
    width: 10rem;
  }

  .options .center input {
    margin-top: 0.3rem;
  }

  .options .right {
    padding: 0.2rem;
    width: 5rem;
    text-align: left;
  }

  .input-text {
    margin: 2rem 0 0.5rem 0;
  }

  .today {
    display: block;
  }

  .disableFont {
    color: #ccc;
  }

  .passwd-title {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 2rem;
    font-weight: 100;
    background-color: #eee;
    padding: 0.5rem;
  }

  .passwd {
    font-size: 1.2em;
    font-weight: 100;
    word-break: break-all;
    padding: 0.5rem;
  }
</style>
